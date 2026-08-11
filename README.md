# Analytics Data Pipeline

An analytics engineering portfolio project showing a testable Python + SQL ETL pipeline. It ingests operational records, validates them, transforms them into analytics-ready tables, and produces KPI queries.

## Pipeline

```text
CSV/Source → Python ingestion → Data quality → SQL transform → Analytics marts
```

## Structure

```text
src/ingest.py
src/transform.py
sql/schema.sql
sql/mart.sql
data/sample_events.csv
tests/test_pipeline.py
.github/workflows/test.yml
```

## Run

```bash
python src/ingest.py
python src/transform.py
```

## KPIs

- daily event volume
- successful vs failed events
- average processing duration
- error rate
- top services by activity

The design separates ingestion, transformation, validation, and analytical SQL so each stage can be tested and operated independently.
