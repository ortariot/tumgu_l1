import uvicorn
from fastapi import FastAPI

app = FastAPI()

LANGUES = {
    1: "c++",
    2: "js",
    3: "python",
}


@app.get("/")
async def root():
    return {"mes": "hello world"}


@app.get("/lang/{item_id}")
async def lang(item_id):
    return {"lang": LANGUES.get(int(item_id), "unknown")}



#"localhost:port/items/1?limit=100&page=1"
@app.get("/sum/")
async def lang(a: int = 0, b: int = 0):
        return {"sum": a+b}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )