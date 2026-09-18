Markdown
# Support Ticket Analytics Platform

An AI-powered support ticket analytics system featuring natural language querying, anomaly detection, a FastAPI REST API, and a Streamlit dashboard.

## Architecture
- **Data Layer (`core/data_loader.py`)**: Ingestion and metric summary extraction.
- **Anomaly Detection (`core/anomaly.py`)**: Identifies stale high-priority tickets and statistical outliers.
- **LLM Engine (`core/llm_service.py`)**: Query interface supporting Groq or fallback analysis.
- **Interfaces**: FastAPI backend (`main.py`) and Streamlit web dashboard (`app.py`).

## Getting Started
```bash
pip install -r requirements.txt
uvicorn main:app --reload
streamlit run app.py
