from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/kilimobora/register")
async def user_registration(name, email, password_hash):
    pass

@app.post("/kilimobora/login")
async def user_login(email, password) -> dict:
    return {
        "message": "Log in successful",
        "status": 200
    }

@app.post("/kilimobora/predict")
async def predict(image: str) -> dict:
    return {
        "message": "",
        "status": 200
    }
