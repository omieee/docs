"""Append harvest rows. Usage: python3 -I add.py acc|exc|co '<json object or list>'"""
import json, sys, pathlib
base = pathlib.Path(__file__).parent
kind, payload = sys.argv[1], json.loads(sys.argv[2])
items = payload if isinstance(payload, list) else [payload]
f = {"acc": "accepted.jsonl", "exc": "excluded.jsonl", "co": "companies.jsonl"}[kind]
with open(base / f, "a") as fh:
    for it in items:
        fh.write(json.dumps(it, ensure_ascii=False) + "\n")
n = sum(1 for _ in open(base / f))
print(f"{f}: {n} rows")
