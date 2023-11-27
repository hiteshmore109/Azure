from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def default():
    return {"success":True, "message":"This is default page"}

@app.get("/home")
def home():
    return {"success":True, "message": "Succesfully loaded page"}

@app.get("/html", response_class = HTMLResponse)
def html():
    return '''
    <h1> THIS IS USING h1 TAG OF HTML</h1>
    <p> Hello, Mom! </p>
    '''