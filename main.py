from fastapi import FastAPI

app = FastAPI(title="Marketplace API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
