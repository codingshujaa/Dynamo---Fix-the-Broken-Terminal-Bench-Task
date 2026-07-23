import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def load_report():
    assert REPORT_PATH.exists(), "missing /app/report.json"
    with REPORT_PATH.open() as f:
        report = json.load(f)
    assert isinstance(report, dict), "report.json must contain a JSON object"
    return report


def test_success_criterion_1_report_has_exact_schema():
    """Success criterion 1: /app/report.json has exactly the requested keys and value types."""
    report = load_report()
    assert set(report) == EXPECTED_KEYS
    assert isinstance(report["total_requests"], int)
    assert isinstance(report["unique_ips"], int)
    assert isinstance(report["top_path"], str)


def test_success_criterion_2_total_requests():
    """Success criterion 2: total_requests counts the non-empty access-log entries."""
    assert load_report()["total_requests"] == 6


def test_success_criterion_3_unique_ips():
    """Success criterion 3: unique_ips counts distinct client IP addresses."""
    assert load_report()["unique_ips"] == 3


def test_success_criterion_4_top_path():
    """Success criterion 4: top_path is the most frequently requested path."""
    assert load_report()["top_path"] == "/index.html"
