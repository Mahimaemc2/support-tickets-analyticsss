Python
import streamlit as st
from core.data_loader import DataLoader
from core.anomaly import AnomalyDetector
from core.llm_service import LLMService

st.title("🎫 AI Support Ticket Dashboard")

loader = DataLoader()
detector = AnomalyDetector(loader)
llm = LLMService()

q = st.text_input("Ask a natural language question about the dataset:")
if st.button("Submit Query") and q:
    with st.spinner("Analyzing..."):
        ctx = loader.get_summary_context()
        st.info(llm.query(q, ctx))

if st.button("Run Anomaly Scan"):
    res = detector.detect_anomalies()
    st.write(f"Found {res['count']} potential anomalies.")
    for a in res["anomalies"]:
        st.warning(f"[{a['type']}] Ticket: {a['ticket_id']} - {a['details']}")
