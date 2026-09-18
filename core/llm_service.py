Python
import os
import requests

class LLMService:
    def __init__(self):
        self.groq_key = os.getenv("GROQ_API_KEY")

    def query(self, question: str, context: str) -> str:
        prompt = f"Context: {context}\n\nQuestion: {question}\nProvide a concise answer based on context."
        
        if self.groq_key:
            try:
                res = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization": f"Bearer {self.groq_key}"},
                    json={"model": "llama-3.1-8b-instant", "messages": [{"role": "user", "content": prompt}]},
                    timeout=5
                )
                if res.status_code == 200:
                    return res.json()["choices"][0]["message"]["content"]
            except Exception:
                pass
