from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Backend working"}

@app.get("/generate")
async def generate():
    return {"message": "Hello from FastAPI backend"}