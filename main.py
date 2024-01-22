from fastapi import FastAPI
from models.BaseModel import init
from routers.v1.AuthorRouter import AuthorRouter

app = FastAPI()



# Add Routers
app.include_router(AuthorRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

init()
