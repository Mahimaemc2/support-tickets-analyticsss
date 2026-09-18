Python
import pandas as pd
from typing import Dict, Any

class AnomalyDetector:
    def __init__(self, data_loader):
        self.loader = data_loader

    def detect_anomalies(self) -> Dict[str, Any]:
        df = self.loader.load_data()
        if df.empty:
            return {"anomalies": [], "count": 0}

        anomalies = []

        if all(col in df.columns for col in ["priority", "status", "created_at"]):
            max_time = df["created_at"].max()
            unresolved = df[df["status"].str.lower().isin(["open", "escalated"])]
            
            for idx, row in unresolved.iterrows():
                hours_open = (max_time - row["created_at"]).total_seconds() / 3600
                if row["priority"] in ["High", "Critical"] and hours_open > 24:
                    anomalies.append({
                        "ticket_id": row["ticket_id"],
                        "type": "Stale High-Priority Ticket",
                        "details": f"Priority {row['priority']} unresolved for {round(hours_open, 1)} hours."
                    })

        if "resolution_time_hrs" in df.columns:
            res_df = df.dropna(subset=["resolution_time_hrs"])
            mean = res_df["resolution_time_hrs"].mean()
            std = res_df["resolution_time_hrs"].std()

            if std > 0:
                outliers = res_df[(res_df["resolution_time_hrs"] - mean) / std > 2.5]
                for idx, row in outliers.iterrows():
                    anomalies.append({
                        "ticket_id": row["ticket_id"],
                        "type": "Abnormally Long Resolution",
                        "details": f"Resolution took {row['resolution_time_hrs']} hrs (Avg: {round(mean, 1)} hrs)."
                    })

        return {"count": len(anomalies), "anomalies": anomalies}
