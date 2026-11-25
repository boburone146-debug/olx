from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Marketly API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Marketly API is running"}

@app.get("/api/products")
def get_products():
    return [
        {
            "id": 1,
            "title": "iPhone 14",
            "price": 2500000,
            "location": "Tashkent"
        }
    ]