from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Detail": "Hello world"}
