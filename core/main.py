Python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.data_loader import DataLoader
from core.anomaly import AnomalyDetector
from core.llm_service import LLMService

app = FastAPI(title="Support Ticket API")

loader = DataLoader()
detector = AnomalyDetector(loader)
llm = LLMService()

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/anomalies")
def anomalies():
    return detector.detect_anomalies()

@app.post("/query")
def ask(payload: QueryRequest):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    ctx = loader.get_summary_context()
    return {"question": payload.question, "answer": llm.query(payload.question, ctx)}
