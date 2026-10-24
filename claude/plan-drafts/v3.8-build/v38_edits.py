# v3.8 edits, layered on the v3.7 layer (Claude, Oct 24 2026). Every target string below is v3.7 output text.
# rep() fails loudly if a target is missing. Sections 4-6 and 14 are edited in their own files.

# ---------- title, header, section 0 ----------
s0 = rep(s0, "# Phase 1 Master Plan v3.7: Portable Skills You Can Prove", "# Phase 1 Master Plan v3.8: Portable Skills You Can Prove")
s0 = rep(s0, "owned production code asked of the manager), effective when Om uploads it · **Replaces:** the v3.6 draft, v3.5,",
         "owned production code asked of the manager), approved by Om on 2026-10-23 · **v3.8 amendment drafted:** 2026-10-24 (use what is taught: a use step in real code for every teaching part, the agent's skeleton from G2, 5-minute session warm-ups and scheduled bedside cards, no row naming an untaught tool, the first spoken stories in W10), effective when Om uploads it · **Replaces:** v3.7, the v3.6 draft, v3.5,")
s0 = rep(s0, "4. **Practise and prove independently.** Om does the unit's task under its AI rules; git evidence, tests or lab output prove execution.",
         "4. **Practise and prove independently.** Om does the unit's task under its AI rules; git evidence, tests or lab output prove execution. Every teaching part ends with its use in real code, PRCP, the agent or PRCP on kind, inside its own hours (section 6, v3.8).")
s0 = rep(s0, "6. **Retain and transfer.** Use only the scheduled retention checks, and include changed examples so recognition becomes transferable understanding rather than memorisation.",
         "6. **Retain and transfer.** Use only the scheduled retention checks, and include changed examples so recognition becomes transferable understanding rather than memorisation. Between them, the 5-minute session warm-up and the bedside cards keep each topic in use (section 6.12, v3.8).")
s0 = rep(s0, "Anything extra (flags, edge cases, extra labs, nice-to-know) goes once to the later-refactor log and is not taught that session.",
         "Anything extra (flags, edge cases, extra labs, nice-to-know) goes once to the later-refactor log and is not taught that session. If the plan line itself names a tool or style that no earlier unit taught, say so, log it as a plan BUG and do not test it (v3.8; the W4 Go rep was the case).")

# ---------- section 1 ----------
s1 = rep(s1, "Forecast (v3.7): Gate A May 2 2027, Gate B Jan 30 2028, Gate C Feb 27 2028,", "Forecast (v3.8): Gate A May 2 2027, Gate B Feb 6 2028, Gate C Mar 5 2028,")
s1 = rep(s1, "814.25 in v3.6, with no ceiling (Om, Oct 23; section 5 ledger). 820.75 in v3.7 |",
         "814.25 in v3.6, with no ceiling (Om, Oct 23; section 5 ledger). 820.75 in v3.7, 834.5 in v3.8 |")
s1 = rep(s1, "\n\n**Unchanged and still frozen**",
         """

**Decisions adopted in v3.8 (Om, Oct 24 2026: F1 to F5 of Claude's audit, and Om's use rule)**

| # | Was (v3.7) | Now (v3.8) | Evidence |
| --- | --- | --- | --- |
| 23 | Taught in a sandbox; used in the project only when a later unit happened to need it | Every teaching part ends with a use step in real code inside its own hours; a topic with no real use within 7 days moves to the week the project needs it; the checker enforces it | Om, Oct 24: built Duplive and GetMyUni in PHP about 12 years ago and cannot recall `print` today; the Oct 24 Go rep lost its syntax after 11 idle days |
| 24 | DSA alone keeps continuous spaced review | A 5-minute blank-page warm-up opens every non-DSA session; bedside cards on day 1, 7 and 28 after each unit closes | v3.7's map did not touch `yield` again for 12 weeks, or the Sep 27 `IN`, `CASE` and subqueries for 16 (Claude's Oct 24 audit, F1 and F2) |
| 25 | The Go agent starts after G7, in March 2027 | Its skeleton grows from G2 (W5), one piece per G unit, in PRCP's `agent/` folder; A1 starts from it | The same audit; Om's use rule |
| 26 | Kubernetes labs on sample apps until PRCP goes onto kind in 1b | D1 right after P1, so K3 to K5 apply their topics to PRCP's own image | Om's use rule |
| 27 | First spoken story in W23 | First two stories told aloud in W10, before calibration interviews need them | Calibration runs from W5 (F5) |

**Unchanged and still frozen**""")

# ---------- section 2 ----------
s2 = rep(s2, "`yield` fixtures 6/6 (Oct 23); MC1 FAIL 2/10.",
         "`yield` fixtures 6/6 (Oct 23); MC1 FAIL 2/10; Go retrieval rep 1 slipped on syntax (`t *testing.T`, `strings.Builder`) after 11 idle days, method held (Oct 24).")

# ---------- section 7 ----------
s7 = rep(s7, "checks due after Gate C carry into Phase 2. DSA alone keeps continuous spaced review. Retrieval reps (section 6.12) are practice, not tests: held or slipped, no score.",
         "checks due after Gate C carry into Phase 2. DSA keeps its spaced re-solves; every other topic is used in real code when taught and comes back in the 5-minute session warm-ups and the bedside cards (v3.8, section 6.12). Retrieval reps and warm-ups (section 6.12) are practice, not tests: held or slipped, no score.")
s7 = rep(s7, "Continuity record: last real use of Go, Kubernetes, LLD, HLD, operators, cloud; any track at its limit",
         "Continuity record: last real use of Go, Kubernetes, LLD, HLD, operators, cloud; any track at its limit\nUse steps and warm-ups (v3.8): use steps done or missed; warm-up slips this week")

# ---------- section 9 ----------
s9 = rep(s9, "4. **Optional cards (v3.6):** short questions from closed units' interviews, read on the phone. Never required, never counted (section 6.12).",
         "4. **Bedside cards (v3.8, scheduled):** 5 to 8 answer-first cards per closed unit, read on the phone on day 1, 7 and 28 after it closes; try each answer before scrolling. No desk hours, no debt (section 6.12).")
s9 = rep(s9, "unit totals equal their track budgets, and no watched track breaks the continuity rule (v3.6).",
         "unit totals equal their track budgets, no watched track breaks the continuity rule (v3.6), every teaching part in the map carries its use step, and no row names a listed tool before the unit that teaches it (v3.8).")
s9 = rep(s9, "Everything else goes to the later-refactor log, logged once.",
         "Everything else goes to the later-refactor log, logged once.\n- **Taught before named (v3.8):** at each rebuild the coach lists every tool, flag and test style named in the next 4 weeks of rows and confirms each was taught before it is used; the checker covers a fixed list of terms.")

# ---------- section 11 ----------
s11 = rep(s11, "Phase 2 starts after Gate C, now forecast Feb 27 2028 (v3.7).", "Phase 2 starts after Gate C, now forecast Mar 5 2028 (v3.8).")
s11 = rep(s11, "an offer around Gate B (now about January 2028) means joining around May 2028.", "an offer around Gate B (now early February 2028) means joining around May 2028.")

# ---------- section 12 ----------
s12 = rep(s12, "| `check_plan.py` | Replace with the v3.7 checker (the v3.6 checks, plus: no coaching-owner wording outside the change log, the human live-coding mock and both harvest slices before Gate B, and the Gate C four-line record) | The v3.5 checker cannot read v3.7 |",
          "| `Phase1_Master_Plan_v3.7.md` (sha256 `31d6753c48138696`) | Remove from both projects once v3.8 is uploaded; it stays in `omieee/docs` git history | Superseded by v3.8 |\n| `check_plan.py` | Replace with the v3.8 checker (the v3.7 checks, plus: every teaching part carries its use step, no row names a listed tool before the unit that teaches it, K3 after D1, and section 7 no longer limits spaced review to DSA) | The v3.7 checker cannot read v3.8's new rules |")
s12 = rep(s12, '"Source of truth: Phase1_Master_Plan_v3.7.md",', '"Source of truth: Phase1_Master_Plan_v3.8.md",')

# ---------- section 13 ----------
s13 = rep(s13, "## 13. Change log: v3 to v3.7", "## 13. Change log: v3 to v3.8")
_c77 = open(os.path.join(D, "change77.md")).read().rstrip()
s13 = rep(s13, _c77, _c77 + "\n\n" + open(os.path.join(D, "change78.md")).read().rstrip())
