from pathlib import Path
import json


def test_report_exists_and_is_json():
    """instruction: Produce a JSON report at /app/report.json"""
    p = Path("/app/report.json")
    assert p.exists(), "no report.json found"
    assert p.stat().st_size > 0, "report.json is empty"
    # ensure it's valid JSON
    with p.open() as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json does not contain a JSON object"


def test_report_keys_and_types():
    """instruction: Report must contain integer total_requests, integer unique_ips, and top_path string or null"""
    p = Path("/app/report.json")
    with p.open() as f:
        data = json.load(f)

    assert "total_requests" in data, "missing total_requests"
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"

    assert "unique_ips" in data, "missing unique_ips"
    assert isinstance(data["unique_ips"], int), "unique_ips must be an integer"

    assert "top_path" in data, "missing top_path"
    assert (isinstance(data["top_path"], str) or data["top_path"] is None), "top_path must be string or null"
