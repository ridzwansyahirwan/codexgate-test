from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CodeXGate setup ready"}


@app.get("/status")
def health():
    return {"status": "ok"}