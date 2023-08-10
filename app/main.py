from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"massage":"Hello world"}

@app.put("/")
def user():
    return{"massage":"user"}

@app.post("/user/{name}")
def user (name):
    return{"massage":"added{0}".format(name)}