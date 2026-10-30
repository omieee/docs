"""Behaviour tests for the draft checker; no replacement plan is generated."""
import unittest

from proposed_rules import DEPS, REQUIRED, check, parse, structural_errors


def fixture():
    """Small dependency-ordered schedule, for rule tests only, not a curriculum."""
    remaining = set.union(*REQUIRED.values()) | {u for pair in DEPS for u in pair}
    ordered = []
    while remaining:
        available = sorted(u for u in remaining if all(p in ordered for d, p in DEPS if d == u))
        if not available:
            raise AssertionError("dependency cycle in checker")
        ordered.extend(available)
        remaining.difference_update(available)
    budgets, weeks = {}, {}
    for i, unit in enumerate(ordered):
        budgets[unit] = 12.0 if unit == "CL3" else 1.0
        weeks[i] = [(unit, 3.0, "") for _ in range(4)] if unit == "CL3" else [(unit, 1.0, "")]
    return budgets, weeks, {"A": [1], "B": [len(weeks) + 1], "C": [len(weeks) + 3]}


class RulesTest(unittest.TestCase):
    def setUp(self):
        self.budget, self.weeks, self.gates = fixture()

    def errors(self):
        return structural_errors(self.budget, self.weeks, self.gates)

    def test_valid_structural_fixture(self):
        self.assertEqual(self.errors(), [])

    def test_each_pillar_cannot_be_removed_from_both_tables(self):
        for pillar, units in REQUIRED.items():
            with self.subTest(pillar=pillar):
                b, w, g = fixture()
                for unit in units:
                    b.pop(unit)
                w = {n: [item for item in items if item[0] not in units] for n, items in w.items()}
                self.assertTrue(any(f"Core: {pillar}" in e for e in structural_errors(b, w, g)))

    def test_budget_without_schedule(self):
        self.weeks = {n: [i for i in items if i[0] != "CL2"] for n, items in self.weeks.items()}
        self.assertIn("Core: AWS and Terraform unit CL2 absent from section 14", self.errors())

    def test_schedule_without_budget(self):
        self.budget.pop("CL1")
        self.assertTrue(any("CL1 absent or unfunded" in e for e in self.errors()))

    def test_zero_budget(self):
        self.budget["A2"] = 0
        self.assertTrue(any("A2 absent or unfunded" in e for e in self.errors()))

    def test_missing_prerequisite(self):
        self.weeks = {n: [i for i in items if i[0] != "D1"] for n, items in self.weeks.items()}
        self.assertTrue(any("no scheduled prerequisite D1" in e for e in self.errors()))

    def test_same_week_reversed_order_rejected(self):
        w = {0: [("CL2", 8.0, ""), ("CL1", 8.0, "")]}
        self.assertTrue(any("Order: CL2 starts" in e for e in structural_errors({}, w, {}, [("CL2", "CL1")])))

    def test_same_week_correct_order_allowed(self):
        w = {0: [("CL1", 8.0, ""), ("CL2", 8.0, "")]}
        self.assertFalse(any("Order: CL2" in e for e in structural_errors({}, w, {}, [("CL2", "CL1")])))

    def test_prerequisite_later_chunk_still_blocks(self):
        w = {0: [("CL1", 4.0, ""), ("CL2", 8.0, ""), ("CL1", 4.0, "")]}
        self.assertTrue(any("Order: CL2 starts" in e for e in structural_errors({}, w, {}, [("CL2", "CL1")])))

    def test_cloud_before_complete_kind_rejected(self):
        w = {0: [("CL3", 3.0, "")], 1: [("K6b", 2.0, "")]}
        self.assertTrue(any("Order: CL3 starts" in e for e in structural_errors({}, w, {}, [("CL3", "K6b")])))

    def test_equal_total_split_cloud_labs_rejected(self):
        w = {0: [("CL3", h, "") for h in (1.5, 3, 3, 3, 1, .5)]}
        self.assertEqual(sum(i[1] for i in w[0]), 12)
        self.assertTrue(any("Cloud labs:" in e for e in structural_errors({}, w, {}, [])))

    def test_three_labs_rejected(self):
        for n, items in self.weeks.items():
            if items and items[0][0] == "CL3":
                self.weeks[n] = items[:3]
        self.assertTrue(any("Cloud labs:" in e for e in self.errors()))

    def test_missing_and_duplicate_gate_rejected(self):
        for g in ([], [1, 2]):
            with self.subTest(g=g):
                self.gates["B"] = g
                self.assertTrue(any("exactly one GATE B" in e for e in self.errors()))

    def test_out_of_order_gates_rejected(self):
        self.gates["A"] = [self.gates["C"][0] + 1]
        self.assertTrue(any("in increasing weeks" in e for e in self.errors()))

    def test_core_finishes_in_gate_week_rejected(self):
        last_cl4 = max(n for n, items in self.weeks.items() if any(i[0] == "CL4" for i in items))
        self.gates["B"] = [last_cl4]
        self.assertTrue(any("CL4 must finish before Gate B" in e for e in self.errors()))

    def test_missing_section_readable_failure(self):
        self.assertEqual(check("# empty"), ["Schema: missing section 6"])

    def test_malformed_week_rejected(self):
        s = "## 6. Curriculum by track\n\n## 14. Week map from Oct 1\n| W4 broken |\n"
        self.assertIn("Schema: malformed or absent week rows", parse(s)[3])

    def test_duplicate_week_rejected(self):
        row = "| W4 · Oct 26-Nov 1 · 1h | **G1** 1h: example | Work |\n"
        s = "## 6. Curriculum by track\n## 14. Week map from Oct 1\n" + row + row
        self.assertIn("Schema: duplicate W4", parse(s)[3])

    def test_duplicate_budget_rejected(self):
        row = "| G1 Basics | 1 | Example | Proof |\n"
        s = "## 6. Curriculum by track\n" + row + row + "## 14. Week map from Oct 1\n"
        self.assertIn("Schema: duplicate unit G1", parse(s)[3])

    def test_zero_hour_row_rejected(self):
        s = "## 6. Curriculum by track\n## 14. Week map from Oct 1\n| W0 · Oct 1-4 · 0h | **G1** 0h: example | Work |\n"
        self.assertIn("Schema: W0 G1 must have positive hours", parse(s)[3])

    def test_unparsed_item_rejected(self):
        s = "## 6. Curriculum by track\n## 14. Week map from Oct 1\n| W0 · Oct 1-4 · 1h | **G1** one hour: example | Work |\n"
        self.assertIn("Schema: W0 has an unparsed item", parse(s)[3])

    def test_cloud_must_be_explicitly_protected(self):
        s = "## 5. Track priorities\n**Never cut:** Go, Kubernetes.\n## 6. Curriculum by track\n## 14. Week map from Oct 1\n| W0 · Oct 1-4 · 1h | **G1** 1h: example | Work |\n"
        self.assertTrue(any("never-cut list" in e for e in check(s)))

    def test_protected_cloud_wording_accepted(self):
        s = "## 5. Track priorities\n**Never cut:** Go, Kubernetes, AWS and Terraform foundations.\n## 6. Curriculum by track\n## 14. Week map from Oct 1\n| W0 · Oct 1-4 · 1h | **G1** 1h: example | Work |\n"
        self.assertFalse(any("never-cut list" in e for e in check(s)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
