from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Semantic Guardian API is running"}
