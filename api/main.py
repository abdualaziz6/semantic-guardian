from fastapi import FastAPI
from validator_rules import rule_check

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Semantic Guardian API running"}

@app.post("/validate")
def validate(data: dict):

    rule_result = rule_check(data)

    if rule_result:
        return {"warning": rule_result}

    return {"status": "ok"}
