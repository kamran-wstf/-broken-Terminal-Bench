import json
import os
import re
from collections import Counter


def generate_report(log_path="/app/access.log", report_path="/app/report.json"):
    paths = Counter()
    ips = set()
    total = 0

    if not os.path.exists(log_path):
        # write empty/zeroed report when input missing
        report = {"total_requests": 0, "unique_ips": 0, "top_path": None}
        with open(report_path, "w") as out:
            json.dump(report, out)
        return report

    method_re = re.compile(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ')
    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 1:
                continue
            total += 1
            ips.add(parts[0])
            m = method_re.search(line)
            if m:
                paths[m.group(1)] += 1

    top_path = paths.most_common(1)[0][0] if paths else None
    report = {"total_requests": total, "unique_ips": len(ips), "top_path": top_path}
    with open(report_path, "w", encoding="utf-8") as out:
        json.dump(report, out)
    return report


if __name__ == "__main__":
    LOG = os.getenv("LOG", "/app/access.log")
    REPORT = os.getenv("REPORT", "/app/report.json")
    r = generate_report(LOG, REPORT)
    print(f"wrote {REPORT}: {r}")
