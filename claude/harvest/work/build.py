"""Build Claude's harvest CSV and Excel from accepted.jsonl and excluded.jsonl.

Run: python3 -I build.py   (from this folder)
Outputs: ../2026-10-27-claude.csv and ../2026-10-27-claude.xlsx
"""
import csv, json, re, datetime, pathlib, collections
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter

BASE = pathlib.Path(__file__).parent
OUT = BASE.parent
RETRIEVED = datetime.date(2026, 10, 27)
HEADER = ("id,company_no,region,country,city,employer,title,req_id,url,source,retrieved,posted,status,"
          "work_summary,build_share,level,years_asked,langs_required,langs_alt_or_optional,skills_required,"
          "skills_preferred,lane,prod_history_screen,om_evidence,work_model,pay_stated,english_team,local_language,"
          "language_years_screen,interview_format,where_held,india_candidates,ai_infra,ai_terms,ai_req,helm,"
          "public_cloud,terraform,k8s_controllers,notes").split(",")

# Rows withdrawn because the employer is on ChatGPT's company list (spec section 1 and 2.4).
WITHDRAWN = {"CL-043": "G008 StarTree", "CL-053": "G008 StarTree", "CL-070": "G025 GitLab"}

# Hand coding from each row's langs_required and langs_alt_or_optional (Claude, Oct 27).
# required = the job names this language with no alternative; allowed = one of the languages that
# satisfies the requirement; preferred = optional or a plus; none = not named.
GO = {}
PY = {}
for ids, val in [("001 002 008 012 017 019 023 026 028 029 031 037 038 042 044 052 063 066 067", "required"),
                 ("004 005 006 007 009 015 016 018 020 022 024 025 027 030 032 033 035 036 040 043 046 047 048 "
                  "050 051 057 058 064 068 069 071 072 073", "allowed"),
                 ("003 010 021 056 059", "preferred")]:
    for i in ids.split():
        GO["CL-" + i] = val
for ids, val in [("001 049 054 060 062", "required"),
                 ("004 005 006 007 009 011 013 014 016 018 020 022 024 025 030 032 033 035 040 041 046 048 050 "
                  "057 058 068 071 072 073", "allowed"),
                 ("002 010 026 029 039 051 056 059 061 067", "preferred")]:
    for i in ids.split():
        PY["CL-" + i] = val
# Rows from Om's LinkedIn or Naukri captures go to their own sheets and are not part of the
# company-page sample that the Summary counts: they come from Om's alerts, not the lane strings.
OM_SOURCES = ("Om LinkedIn", "LinkedIn lead", "Om Naukri", "Naukri lead")
PRODUCT_BACKEND = set("CL-" + i for i in "016 018 022 036 038 040 049 054 057 060 070 072 073".split())

# Manual notes for listed companies, from pages read on Oct 27.
COMPANY_NOTES = {
    "C071": "Searched (search engine and readable boards): no readable Flipkart posting found; likely LinkedIn, Naukri or own portal. Needs Om's LinkedIn/Naukri capture.",
    "C073": "Searched: results were Instahyre and aggregator pages (unreadable or not the employer); one Greenhouse link was a 1-3 year role. Needs Om's capture.",
    "C075": "CRED Lever board read: only 2 engineering roles, both security (Cloud Security, Threat Detection). No fitting role.",
    "C076": "Searched: no readable Groww posting found. Needs Om's capture.",
    "C077": "Searched: no readable Zerodha posting found. Needs Om's capture.",
    "C080": "Meesho Lever board read: 13 tech roles, mostly managers, data science and security; SDE III Data excluded (5-8 years).",
    "C083": "Juspay careers page is a generic listing with no title, level or date.",
    "C084": "Zeta Lever board read: SRE, network, security and database roles only (some are Zeta Global, US). No fitting role.",
    "C090": "Searched: Dream11 postings found only on Instahyre and startup.jobs (unreadable). Needs Om's capture.",
    "C100": "Dreamwork 'Slice' page could not be tied to the Indian fintech slice; not used.",
    "C020": "Commvault India Greenhouse roles read: C#, C++ and DevOps only, apart from the accepted Clumio backend role.",
    "C072": "Razorpay Greenhouse page 1 read: DevOps, DBA, security and AI builder roles; one Lead SDE accepted.",
}


def posted_norm(raw):
    """Return (posted, age_evidence, note). posted is YYYY-MM-DD or 'unknown'."""
    raw = (raw or "unknown").strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return raw, "date", ""
    if raw.startswith("unknown") or raw.startswith("updated"):
        return "unknown", ("updated-only" if "updated" in raw else ("indexed" if "indexed" in raw else "none")), \
            ("" if raw == "unknown" else "posted field: " + raw)
    m = re.match(r"(?:about )?(same day|one day|\d+ days?) before retrieval|same day as retrieval", raw)
    if m:
        txt = raw
        n = 0 if "same day" in txt else (1 if "one day" in txt else int(re.search(r"\d+", txt).group()))
        return (RETRIEVED - datetime.timedelta(days=n)).isoformat(), "date", "posted computed from: " + raw
    return "unknown", "relative-weeks", "posted per mirror: " + raw


def load(name):
    return [json.loads(l) for l in open(BASE / name)]


acc_raw = load("accepted.jsonl")
exc_raw = load("excluded.jsonl")
companies = list(csv.DictReader(open(OUT / "2026-10-27-companies-claude.csv")))
cg_companies = list(csv.DictReader(open(OUT.parent.parent / "chatgpt" / "harvest" / "2026-10-27-companies-chatgpt.csv")))
cg_names = {r["company"].lower(): r["no"] for r in cg_companies}

accepted, coding, withdrawn_rows = [], [], []
for d in acc_raw:
    row = {k: d.get(k, "") for k in HEADER}
    row.update(region="India", country="India", retrieved=d.get("retrieved") or RETRIEVED.isoformat(), status="open")
    row["pay_stated"] = d.get("pay_stated") or "unknown"
    for k in ("english_team", "local_language", "language_years_screen", "interview_format", "where_held", "india_candidates"):
        row[k] = "n/a"
    for k in ("ai_infra",):
        row[k] = row[k] or "none"
    for k in ("ai_req", "helm", "terraform", "k8s_controllers"):
        row[k] = row[k] or "none"
    row["ai_terms"] = row["ai_terms"] or "none"
    posted, age, pnote = posted_norm(d.get("posted"))
    row["posted"] = posted
    if pnote:
        row["notes"] = (row["notes"] + "; " if row["notes"] else "") + pnote
    if row["id"] in WITHDRAWN:
        withdrawn_rows.append((row, WITHDRAWN[row["id"]]))
        continue
    accepted.append(row)
    if row["source"].startswith(OM_SOURCES):
        continue  # Om's captures: own sheet, kept out of the sample counts (spec v2.1 s8)
    yrs = re.search(r"\d+", row["years_asked"] or "")
    prod = (row["prod_history_screen"] or "").lower()
    cloud_txt_req = row["skills_required"]
    cloud_re = r"\b(AWS|Azure|GCP|Google Cloud|OCI|hyperscaler|public cloud|cloud provider|cloud platform)"
    if re.search(cloud_re, cloud_txt_req, re.I):
        cloud = "required"
    elif re.search(cloud_re, row["skills_preferred"], re.I):
        cloud = "preferred"
    elif re.search(cloud_re, row["public_cloud"] + " " + row["work_summary"], re.I):
        cloud = "named only"
    else:
        cloud = "none"
    aws = "yes" if re.search(r"\bAWS\b|Amazon Web Services|\bEKS\b", " ".join(
        [row["skills_required"], row["skills_preferred"], row["public_cloud"], row["work_summary"]])) else "no"
    k8s_txt = " ".join([row["skills_required"], row["skills_preferred"]])
    if re.search(r"Kubernetes|\bEKS\b|\bGKE\b|\bAKS\b|OpenShift", row["skills_required"]):
        k8s = "required"
    elif re.search(r"Kubernetes|\bEKS\b|\bGKE\b|\bAKS\b|OpenShift", row["skills_preferred"]):
        k8s = "preferred"
    elif re.search(r"Kubernetes", row["work_summary"] + row["title"]):
        k8s = "duties only"
    else:
        k8s = "none"
    coding.append({
        "id": row["id"], "employer": row["employer"], "company_no": row["company_no"], "lane": row["lane"],
        "go": GO.get(row["id"], "none"), "python": PY.get(row["id"], "none"),
        "kubernetes": k8s, "cloud": cloud, "aws_named": aws,
        "prod_screen": "no" if (prod.startswith("none") or prod == "") else "yes",
        "years_min": int(yrs.group()) if yrs else "",
        "band_risk": "yes" if (yrs and int(yrs.group()) <= 4) else "no",
        "product_backend": "yes" if row["id"] in PRODUCT_BACKEND else "no",
        "build_share": row["build_share"], "age_evidence": age,
        "level_stretch": "yes" if re.search(r"Senior Staff|Sr Staff|Principal", row["level"] + row["title"]) else "no",
        "source_web": "yes" if row["company_no"] == "web" else "no",
    })

# Excluded rows: withdrawn first, then the rest.
excluded = []
for row, g in withdrawn_rows:
    excluded.append({"company_no": row["company_no"], "employer": row["employer"], "title": row["title"],
                     "url": row["url"], "retrieved": RETRIEVED.isoformat(),
                     "reason": f"withdrawn: company is on ChatGPT's list ({g}); Claude had classified it as lane {row['lane']}, ai_infra {row['ai_infra']}; handed over, not counted by Claude"})
for d in exc_raw:
    excluded.append({k: d.get(k, "") for k in ("company_no", "employer", "title", "url", "retrieved", "reason")})
for i, e in enumerate(excluded, 1):
    e["id"] = f"EX-{i:03d}"
    nm = e["employer"].lower()
    e["chatgpt_list"] = next((no for n, no in cg_names.items() if n in nm or nm.split(" (")[0] == n), "")


def reason_cat(r):
    r = r.lower()
    for key, pat in [("withdrawn (ChatGPT company)", r"^withdrawn"), ("unread or unverifiable", r"unread|unreadable|unverifiable"),
                     ("closed or removed", r"closed|removed|no longer"), ("older than 3 months", r"older than 3 months"),
                     ("not India", r"not india"), ("junior", r"junior"),
                     ("other language required", r"(java|jvm|c\+\+|node\.js|kotlin|c#|javascript)[^;]*required"),
                     ("SRE, DevOps or ops duties", r"\bsre\b|devops|operations|ops duties"),
                     ("years outside fit", r"years ")]:
        if re.search(pat, r):
            return key
    return "role identity (not backend infrastructure)"


for e in excluded:
    e["reason_group"] = reason_cat(e["reason"])

# ---------- validation ----------
errors = []
urls = collections.Counter(r["url"] for r in accepted)
errors += [f"duplicate url {u}" for u, n in urls.items() if n > 1]
for r in accepted:
    if len(r) != len(HEADER):
        errors.append(f"field count {r['id']}")
    if r["lane"] not in "abcd" or not r["lane"]:
        errors.append(f"lane {r['id']}")
    nm = r["employer"].lower()
    if any(n == nm.split(" (")[0] or n in nm for n in cg_names):
        errors.append(f"ChatGPT company in accepted: {r['id']} {r['employer']}")
    if not (re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["posted"]) or r["posted"] == "unknown"):
        errors.append(f"posted format {r['id']}")
acc_urls = set(urls)
for e in excluded:
    if e["url"] in acc_urls and not e["reason"].startswith("withdrawn"):
        errors.append(f"url both accepted and excluded: {e['url']}")
print("validation errors:", errors or "none")

# ---------- CSV ----------
with open(OUT / "2026-10-27-claude.csv", "w", newline="") as fh:
    w = csv.writer(fh, quoting=csv.QUOTE_ALL)
    w.writerow(HEADER)
    for r in accepted:
        w.writerow([r[k] for k in HEADER])

# ---------- Excel ----------
F = "Arial"
bold = Font(name=F, bold=True)
norm = Font(name=F)
head_fill = PatternFill("solid", fgColor="DDE7F0")
wb = Workbook()


def sheet(title, header, rows, widths=None):
    ws = wb.create_sheet(title)
    ws.append(header)
    for c in ws[1]:
        c.font = bold
        c.fill = head_fill
        c.alignment = Alignment(wrap_text=True, vertical="top")
    for r in rows:
        ws.append(r)
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.font = norm
            c.alignment = Alignment(wrap_text=False, vertical="top")
    ws.freeze_panes = "B2"
    for i, h in enumerate(header, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(h, 18)
    return ws


wb.remove(wb.active)
# Companies
acc_n = collections.Counter(r["company_no"] for r in accepted)
exc_n = collections.Counter(e["company_no"] for e in excluded)
comp_rows = []
for c in companies:
    n = c["no"]
    a, x = acc_n[n], exc_n[n]
    if n in COMPANY_NOTES:
        note = COMPANY_NOTES[n]
    elif a:
        note = f"{a} accepted"
    elif x:
        grp = collections.Counter(e["reason_group"] for e in excluded if e["company_no"] == n).most_common(2)
        note = "no fitting posting read; exclusions: " + ", ".join(f"{k} {v}" for k, v in grp)
    else:
        note = "not reached in this run; check LinkedIn/Naukri (Om) and re-run in W6"
    searched = "2026-10-27" if (a or x or n in COMPANY_NOTES) else ""
    comp_rows.append([n, c["company"], c["group"], searched, a + x, a, note])
web = collections.OrderedDict()
for r in accepted:
    if r["company_no"] == "web":
        web.setdefault(r["employer"], [0, 0])[0] += 1
for e in excluded:
    if e["company_no"] == "web":
        web.setdefault(e["employer"], [0, 0])[1] += 1
for emp, (a, x) in web.items():
    comp_rows.append(["web", emp, "wider internet (section 2.4)", "2026-10-27", a + x, a,
                      ("on ChatGPT's list: rows withdrawn" if any(n in emp.lower() for n in cg_names) else "")])
sheet("Companies", ["no", "company", "group", "searched_on", "postings_read", "accepted", "result_note"], comp_rows,
      {"company": 26, "group": 24, "result_note": 90})
# JDs
sample = [r for r in accepted if not r["source"].startswith(OM_SOURCES)]
li_rows = [r for r in accepted if r["source"] in ("Om LinkedIn", "LinkedIn lead")]
nk_rows = [r for r in accepted if r["source"] in ("Om Naukri", "Naukri lead")]
ws = sheet("JDs", HEADER, [[r[k] for k in HEADER] for r in sample],
           {"title": 40, "url": 40, "work_summary": 60, "skills_required": 60, "skills_preferred": 50, "notes": 60, "employer": 22})
nj = len(sample) + 1
# LinkedIn, Naukri, AI probe: header only
for t, rows, note in [("LinkedIn", li_rows, "Rows from Om's LinkedIn captures only (spec v2.1 section 8); Claude's tools are refused by LinkedIn. Raw pastes: claude/harvest/linkedin/. Not in the Summary sample counts."),
                ("Naukri", nk_rows, "Rows from Om's Naukri captures only (spec v2.1 section 8); Claude's tools are refused by Naukri. Not in the Summary sample counts."),
                ("AI probe", [], "Not run in this pass. No AI-infrastructure search string was used for the counted sample (spec section 3).")]:
    s = sheet(t, HEADER, [[r[k] for k in HEADER] for r in rows],
              {"title": 40, "url": 40, "work_summary": 60, "skills_required": 60, "skills_preferred": 50, "notes": 60, "employer": 22})
    s["A1"].comment = Comment(note, "Claude")
# Excluded
sheet("Excluded", ["id", "company_no", "employer", "title", "url", "retrieved", "reason", "reason_group", "chatgpt_list"],
      [[e["id"], e["company_no"], e["employer"], e["title"], e["url"], e["retrieved"], e["reason"], e["reason_group"], e["chatgpt_list"]] for e in excluded],
      {"employer": 24, "title": 44, "url": 44, "reason": 70, "reason_group": 30})
ne = len(excluded) + 1
# Coding (helper for Summary formulas)
ck = list(coding[0].keys())
sheet("Coding", ck, [[c[k] for k in ck] for c in coding], {"employer": 24})
nc = len(coding) + 1

# Summary with live formulas
S = wb.create_sheet("Summary", 0)
S.column_dimensions["A"].width = 58
for col in "BCDEF":
    S.column_dimensions[col].width = 14
S.column_dimensions["G"].width = 70


def W(r, c, v, b=False):
    cell = S.cell(row=r, column=c, value=v)
    cell.font = bold if b else norm
    return cell


W(1, 1, "Claude JD harvest, run 1 (India), retrieved 2026-10-27", True)
W(2, 1, "Spec: claude/harvest/HARVEST-SPEC-2026-10.md v2.1. All counts below are live formulas over the JDs, Coding and Excluded sheets.")
W(3, 1, "z for 95% range"); W(3, 2, 1.96)
S["B3"].font = Font(name=F, color="0000FF")
W(3, 7, "Input: z value for a 95% Wilson score interval.")
W(5, 1, "Item", True); W(5, 2, "Count", True); W(5, 3, "Of", True); W(5, 4, "Share", True); W(5, 5, "95% low", True); W(5, 6, "95% high", True); W(5, 7, "How counted", True)
lines = [
    ("Accepted India JDs", f"=COUNTA(JDs!A2:A{nj})", None, "Rows in JDs (withdrawn ChatGPT-company rows removed)."),
    ("Excluded postings read", f"=COUNTA(Excluded!A2:A{ne})", None, "Rows in Excluded, incl. 3 withdrawn and unread pages."),
    ("Lane a: Python-led backend infrastructure", f'=COUNTIF(JDs!V2:V{nj},"a")', "acc", "lane column"),
    ("Lane b: Go and Kubernetes platform", f'=COUNTIF(JDs!V2:V{nj},"b")', "acc", "lane column"),
    ("Lane c: controllers and operators", f'=COUNTIF(JDs!V2:V{nj},"c")', "acc", "lane column"),
    ("Lane d: data-infrastructure platforms", f'=COUNTIF(JDs!V2:V{nj},"d")', "acc", "lane column"),
    ("Go required (no alternative)", f'=COUNTIF(Coding!E2:E{nc},"required")', "acc", "hand-coded from langs fields"),
    ("Go required or one allowed choice", f'=COUNTIF(Coding!E2:E{nc},"required")+COUNTIF(Coding!E2:E{nc},"allowed")', "acc", "Go satisfies the language requirement"),
    ("Go named at all (incl. preferred)", f'=COUNTIF(Coding!E2:E{nc},"<>none")', "acc", ""),
    ("Python required (no alternative)", f'=COUNTIF(Coding!F2:F{nc},"required")', "acc", "hand-coded from langs fields"),
    ("Python required or one allowed choice", f'=COUNTIF(Coding!F2:F{nc},"required")+COUNTIF(Coding!F2:F{nc},"allowed")', "acc", "Python satisfies the language requirement"),
    ("Python named at all (incl. preferred)", f'=COUNTIF(Coding!F2:F{nc},"<>none")', "acc", ""),
    ("Kubernetes required", f'=COUNTIF(Coding!G2:G{nc},"required")', "acc", "named in skills_required"),
    ("Kubernetes required or preferred", f'=COUNTIF(Coding!G2:G{nc},"required")+COUNTIF(Coding!G2:G{nc},"preferred")', "acc", ""),
    ("Kubernetes controllers or operators required", f'=COUNTIF(JDs!AM2:AM{nj},"required")', "acc", "k8s_controllers column"),
    ("Kubernetes controllers required or preferred", f'=COUNTIF(JDs!AM2:AM{nj},"required")+COUNTIF(JDs!AM2:AM{nj},"preferred")', "acc", ""),
    ("Helm required", f'=COUNTIF(JDs!AJ2:AJ{nj},"required")', "acc", "helm column"),
    ("Helm required or preferred", f'=COUNTIF(JDs!AJ2:AJ{nj},"required")+COUNTIF(JDs!AJ2:AJ{nj},"preferred")', "acc", "decides v3.9 F4 together with Om's bar"),
    ("Terraform required", f'=COUNTIF(JDs!AL2:AL{nj},"required")', "acc", "terraform column"),
    ("Terraform required or preferred", f'=COUNTIF(JDs!AL2:AL{nj},"required")+COUNTIF(JDs!AL2:AL{nj},"preferred")', "acc", ""),
    ("Public cloud required", f'=COUNTIF(Coding!H2:H{nc},"required")', "acc", "any provider named in skills_required"),
    ("Public cloud required or preferred", f'=COUNTIF(Coding!H2:H{nc},"required")+COUNTIF(Coding!H2:H{nc},"preferred")', "acc", ""),
    ("AWS named anywhere in the JD", f'=COUNTIF(Coding!I2:I{nc},"yes")', "acc", "skills, cloud or duties"),
    ("Production-history screen stated", f'=COUNTIF(Coding!J2:J{nc},"yes")', "acc", "prod_history_screen not none"),
    ("ai_infra none", f'=COUNTIF(JDs!AG2:AG{nj},"none")', "acc", ""),
    ("ai_infra app (LLM features, RAG, agents)", f'=COUNTIF(JDs!AG2:AG{nj},"app")', "acc", ""),
    ("ai_infra platform (GPU, serving, inference on Kubernetes)", f'=COUNTIF(JDs!AG2:AG{nj},"platform")', "acc", ""),
    ("ai_infra engine (CUDA, kernels)", f'=COUNTIF(JDs!AG2:AG{nj},"engine")', "acc", ""),
    ("AI requirement marked required", f'=COUNTIF(JDs!AI2:AI{nj},"required")', "acc", "includes 'use AI tools in engineering' lines"),
    ("AI requirement marked preferred", f'=COUNTIF(JDs!AI2:AI{nj},"preferred")', "acc", ""),
    ("Product backend rather than infrastructure", f'=COUNTIF(Coding!M2:M{nc},"yes")', "acc", "hand-tagged"),
    ("Build share 'half' (ops share large)", f'=COUNTIF(Coding!N2:N{nc},"half")', "acc", ""),
    ("Band risk: minimum years 4 or fewer", f'=COUNTIF(Coding!L2:L{nc},"yes")', "acc", "may sit below the 42L fixed gate"),
    ("Stretch level (Senior Staff or Principal)", f'=COUNTIF(Coding!P2:P{nc},"yes")', "acc", ""),
    ("Wider-internet employer (company_no web)", f'=COUNTIF(JDs!B2:B{nj},"web")', "acc", "not on Claude's 100 list"),
    ("Posted date known (exact or day-level)", f'=COUNTIF(Coding!O2:O{nc},"date")', "acc", "posted column has a date"),
    ("Posted only as weeks or a month ago (mirror)", f'=COUNTIF(Coding!O2:O{nc},"relative-weeks")', "acc", "recent, date unknown"),
    ("No posted date (open on retrieval)", f'=COUNTIF(Coding!O2:O{nc},"none")+COUNTIF(Coding!O2:O{nc},"updated-only")+COUNTIF(Coding!O2:O{nc},"indexed")', "acc", "kept per spec 3; re-check in W6"),
]
r = 6
for label, f, of, how in lines:
    W(r, 1, label)
    W(r, 2, f)
    if of == "acc":
        W(r, 3, "=$B$6")
        W(r, 4, f"=IF(C{r}=0,0,B{r}/C{r})").number_format = "0.0%"
        lo = f"=IF(C{r}=0,0,(D{r}+$B$3^2/(2*C{r})-$B$3*SQRT(D{r}*(1-D{r})/C{r}+$B$3^2/(4*C{r}^2)))/(1+$B$3^2/C{r}))"
        hi = f"=IF(C{r}=0,0,(D{r}+$B$3^2/(2*C{r})+$B$3*SQRT(D{r}*(1-D{r})/C{r}+$B$3^2/(4*C{r}^2)))/(1+$B$3^2/C{r}))"
        W(r, 5, lo).number_format = "0.0%"
        W(r, 6, hi).number_format = "0.0%"
    W(r, 7, how)
    r += 1
r += 1
W(r, 1, "Exclusions by reason group", True); r += 1
groups = ["closed or removed", "older than 3 months", "not India", "other language required", "SRE, DevOps or ops duties",
          "years outside fit", "junior", "role identity (not backend infrastructure)", "unread or unverifiable", "withdrawn (ChatGPT company)"]
gstart = r
for g in groups:
    W(r, 1, g)
    W(r, 2, f'=COUNTIF(Excluded!H2:H{ne},A{r})')
    r += 1
W(r, 1, "Total (should equal Excluded postings read)")
W(r, 2, f"=SUM(B{gstart}:B{r-1})")
r += 2
W(r, 1, "Lane-size check (plan section 8)", True); r += 1
W(r, 1, "India roles that fit (accepted)"); W(r, 2, "=B6"); r += 1
W(r, 1, "Of these, below the band-risk line (min years 4 or fewer)"); W(r, 2, f"=B{6 + [l[0] for l in lines].index('Band risk: minimum years 4 or fewer')}"); r += 1
W(r, 1, "Employer-stated fixed pay seen"); W(r, 2, 0)
S.cell(row=r, column=2).font = Font(name=F, color="0000FF")
W(r, 7, "Input: no accepted India posting states pay; mirror estimates are excluded by the spec."); r += 1
W(r, 1, "Trigger fires if fewer than 20 fitting India roles"); W(r, 2, f'=IF(B{r-3}<20,"FIRES","does not fire on count")'); r += 1
W(r, 7, "Count only. Whether each role can meet the 42L fixed gate is not provable from the JDs; see the Levels.fyi snapshot below."); r += 2
W(r, 1, "Levels.fyi Bengaluru Senior SWE snapshot (total comp)", True); r += 1
for lab, val in [("Retrieved", "2026-10-27 (page says updated Oct 26, 2026)"), ("25th percentile", "INR 38.6L"), ("Median", "INR 56.2L"),
                 ("75th percentile", "INR 80.3L"), ("90th percentile", "INR 106.6L"), ("Data points", "4,830"),
                 ("Basis", "total compensation (base + yearly stock + bonus); the 42L gate is fixed cash, so not directly comparable"),
                 ("Source", "https://www.levels.fyi/t/software-engineer/levels/senior/locations/bengaluru-ind"),
                 ("Plan section 3 value (Dec 2025)", "25th 36.3L, median 53.5L, 75th 77.4L")]:
    W(r, 1, lab); W(r, 2, val); r += 1
r += 1
W(r, 1, "Om's captures (outside the sample above)", True); r += 1
W(r, 1, "Accepted from Om's LinkedIn captures"); W(r, 2, f"=COUNTA(LinkedIn!A2:A{len(li_rows) + 1})" if li_rows else 0); W(r, 7, "LinkedIn sheet; from Om's alerts, not the lane strings"); r += 1
W(r, 1, "Accepted from Om's Naukri captures"); W(r, 2, f"=COUNTA(Naukri!A2:A{len(nk_rows) + 1})" if nk_rows else 0); W(r, 7, "Naukri sheet"); r += 2
W(r, 1, "Limits of this sample", True); r += 1
for t in ["LinkedIn and Naukri unreadable by Claude's tools: Indian product companies (Flipkart, PhonePe, CRED, Groww, Zerodha, Dream11 and others) are under-represented.",
          "Readable sources skew to GCCs and SaaS on Greenhouse, Lever, Workday mirrors (Dreamwork), Built In and Getro boards.",
          "Search strings targeted platform, Kubernetes, Go and Python backend roles, so lane and skill shares describe this filtered set, not the whole market.",
          "Coding of Go, Python, product-backend and band risk is Claude's hand coding; every row keeps its source wording in JDs.",
          "IDs CL-043, CL-053 and CL-070 are withdrawn (company on ChatGPT's list), so JDs has gaps in numbering."]:
    W(r, 1, t); r += 1

wb.save(OUT / "2026-10-27-claude.xlsx")
print("accepted", len(accepted), "excluded", len(excluded), "web employers", len(web))
