from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def main():
    return {"endpoint": "main"}

@app.get("/health")
def healt():
    return {"endpoint": "health"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=3001, host='0.0.0.0', reload=True)