#!/usr/bin/env python3
"""Validate the data files: every CSV has rows and the declared columns, and nothing looks like a phone, email or key."""
import csv, json, re, sys, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pkg = json.load(open(os.path.join(root, "datapackage.json")))
# phones (Israeli 0x / +972 or any + prefixed run of 8+ digits), emails and key-like tokens; ISO dates and plain numbers pass
bad = re.compile(r"(?<![\w-])(\+?972|0[2-9])[\d\-\s().]{7,}\d|(?<![\w-])\+\d[\d\-\s]{7,}\d|[\w.+-]+@[\w-]+\.[\w.-]+|sgk_[0-9a-f]{8}|api[_-]?key|secret|bearer ", re.I)
ok = True
for r in pkg["resources"]:
    path = os.path.join(root, r["path"])
    if r["format"] != "csv":
        json.load(open(path)); print("ok json", r["path"]); continue
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    fields = [f["name"] for f in r["schema"]["fields"]]
    if not rows or list(rows[0].keys()) != fields:
        print("FAIL", r["path"], "rows", len(rows)); ok = False; continue
    hits = [v for row in rows for v in row.values() if v and bad.search(v) and "semerenkogroup.com" not in v and "data.gov.il" not in v and "boi.org.il" not in v]
    if hits:
        print("FAIL", r["path"], "suspicious values:", hits[:3]); ok = False; continue
    print("ok", r["path"], len(rows), "rows")
sys.exit(0 if ok else 1)
