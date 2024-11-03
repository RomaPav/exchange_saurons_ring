import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from controller.price_controller import router as price_api

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://front-saurons-ring.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Welcome to my API!"}


app.include_router(price_api, prefix="/price")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True)
