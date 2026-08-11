from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "sample_events.csv"


def load_events():
    with INPUT.open(newline="") as handle:
        return list(csv.DictReader(handle))


def summarize(events):
    services = Counter(row["service"] for row in events)
    failures = sum(row["status"] != "success" for row in events)
    return {
        "events": len(events),
        "failures": failures,
        "error_rate": failures / len(events) if events else 0,
        "top_service": services.most_common(1)[0][0] if services else None,
    }


if __name__ == "__main__":
    print(summarize(load_events()))
