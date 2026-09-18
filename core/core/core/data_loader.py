Python
import pandas as pd
from typing import Optional

class DataLoader:
    def __init__(self, filepath: str = "support_tickets.csv"):
        self.filepath = filepath
        self._df: Optional[pd.DataFrame] = None

    def load_data(self) -> pd.DataFrame:
        if self._df is None:
            try:
                self._df = pd.read_csv(self.filepath)
                if "created_at" in self._df.columns:
                    self._df["created_at"] = pd.to_datetime(self._df["created_at"])
            except Exception as e:
                print(f"Error loading CSV: {e}")
                self._df = pd.DataFrame()
        return self._df

    def get_summary_context(self) -> str:
        df = self.load_data()
        if df.empty:
            return "Dataset is empty or missing."

        total = len(df)
        status_counts = df["status"].value_counts().to_dict() if "status" in df else {}
        prio_counts = df["priority"].value_counts().to_dict() if "priority" in df else {}
        avg_res = round(df["resolution_time_hrs"].dropna().mean(), 2) if "resolution_time_hrs" in df else 0
        
        return f"Total Tickets: {total} | Statuses: {status_counts} | Priorities: {prio
