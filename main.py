from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Okay Tested.!"}

# created a new version
# Made another change

# commit from here
