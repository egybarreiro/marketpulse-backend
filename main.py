from fastapi import FastAPI
from routers.ticker_router import router as ticker_router
from routers.model_router import router as model_router
from routers.data_router import router as data_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ticker_router)
app.include_router(model_router)
app.include_router(data_router)
