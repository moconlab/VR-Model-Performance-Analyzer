from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="VR Model Performance Analyzer")

app.include_router(router)


@app.get("/")
def health():
    return {"status": "ok"}
