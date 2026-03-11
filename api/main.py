from fastapi import FastAPI
from orchestrator import orchestrate_validation
import traceback

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Semantic Guardian API running"}

@app.post("/validate")
def validate(data: dict):
    try:
        result = orchestrate_validation(data)
        return result
    except Exception as e:
        return {
            "status": "error",
            "confidence_score": 0.0,
            "message": str(e),
            "suggestion": traceback.format_exc(),
            "source": "backend"
        }