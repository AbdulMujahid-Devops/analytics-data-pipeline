# Analytics Data Pipeline

> **About:** Python and SQL analytics engineering pipeline for data ingestion, validation, transformation, KPI generation, and analytics-ready reporting. The project connects data engineering practices with operational DevOps use cases.

## What this project demonstrates

The pipeline takes raw operational records through a controlled sequence of ingestion, validation, transformation, and analytical modeling. Each stage has a clear responsibility so failures can be identified, tested, and improved independently.

### Pipeline flow

```text
Raw Source / CSV
      ↓
Python Ingestion
      ↓
Data Validation & Quality Checks
      ↓
Transformation
      ↓
SQL Analytics Models
      ↓
KPI / Reporting Layer
```

### Key capabilities
- Python-based ingestion and transformation
- SQL schema and analytical marts
- Data-quality validation
- Testable pipeline stages
- Operational KPI generation
- Error-rate and processing-duration analysis
- GitHub Actions validation
- Clear separation of ingestion, transformation, and analytics

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

- Daily event volume
- Successful vs failed events
- Average processing duration
- Error rate
- Top services by activity

## DevOps connection

Operational analytics can help engineering teams understand service health, failure patterns, processing performance, and workload behavior. This project therefore demonstrates the intersection of **analytics engineering, automation, data quality, and DevOps observability**.
