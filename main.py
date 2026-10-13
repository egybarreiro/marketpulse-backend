from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.ticker_router import router as ticker_router

app = FastAPI(title="MarketPulse Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ticker_router)
