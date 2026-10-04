"""Reject generated offer data that would roll the committed scan timestamp backward."""
import json
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "offers.json"


def parse_time(value):
    if not value:
        raise ValueError("missing source_scan_at")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main():
    current = json.loads(DATA.read_text(encoding="utf-8"))
    current_time = parse_time(current.get("source_scan_at"))
    previous_raw = subprocess.run(
        ["git", "show", "HEAD:data/offers.json"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout
    previous = json.loads(previous_raw)
    previous_time_value = previous.get("source_scan_at") or previous.get("fetched_at")
    if previous_time_value:
        previous_time = parse_time(previous_time_value)
        if current_time < previous_time:
            raise SystemExit(
                "Refusing to commit stale offer data: "
                f"source_scan_at {current_time.isoformat()} is older than "
                f"committed timestamp {previous_time.isoformat()}"
            )
    for offer in current.get("offers", []):
        fetched_at = offer.get("fetched_at")
        if fetched_at and parse_time(fetched_at) > current_time:
            raise SystemExit(
                f"Refusing to commit offer data: {offer.get('provider', 'unknown')} "
                f"has fetched_at {fetched_at} later than source_scan_at "
                f"{current_time.isoformat()}"
            )
    print(f"Freshness guard passed: {current_time.isoformat()}")


if __name__ == "__main__":
    main()
