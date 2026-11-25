
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

products = [
    {
        "id": 1,
        "title": "iPhone 14",
        "price": 8500000,
        "location": "Tashkent",
        "category": "Electronics",
        "emoji": "📱",
        "description": "Apple iPhone 14, 128GB"
    },
    {
        "id": 2,
        "title": "Samsung Galaxy S24",
        "price": 10500000,
        "location": "Samarkand",
        "category": "Electronics",
        "emoji": "📱",
        "description": "Samsung Galaxy S24, 256GB"
    },
    {
        "id": 3,
        "title": "MacBook Air M2",
        "price": 14500000,
        "location": "Tashkent",
        "category": "Computers",
        "emoji": "💻",
        "description": "Apple MacBook Air M2"
    },
    {
        "id": 4,
        "title": "HP Pavilion Laptop",
        "price": 7800000,
        "location": "Bukhara",
        "category": "Computers",
        "emoji": "💻",
        "description": "HP Pavilion, Intel Core i5"
    },
    {
        "id": 5,
        "title": "AirPods Pro 2",
        "price": 2800000,
        "location": "Tashkent",
        "category": "Accessories",
        "emoji": "🎧",
        "description": "Apple AirPods Pro 2"
    },
    {
        "id": 6,
        "title": "Sony WH-1000XM5",
        "price": 4200000,
        "location": "Samarkand",
        "category": "Accessories",
        "emoji": "🎧",
        "description": "Wireless noise cancelling headphones"
    },
    {
        "id": 7,
        "title": "Nike Air Max",
        "price": 1200000,
        "location": "Tashkent",
        "category": "Fashion",
        "emoji": "👟",
        "description": "Original Nike Air Max sneakers"
    },
    {
        "id": 8,
        "title": "Adidas Ultraboost",
        "price": 1500000,
        "location": "Andijan",
        "category": "Fashion",
        "emoji": "👟",
        "description": "Adidas Ultraboost running shoes"
    },
    {
        "id": 9,
        "title": "Men's Classic Watch",
        "price": 650000,
        "location": "Tashkent",
        "category": "Fashion",
        "emoji": "⌚",
        "description": "Classic men's wristwatch"
    },
    {
        "id": 10,
        "title": "Canon EOS 250D",
        "price": 9200000,
        "location": "Bukhara",
        "category": "Electronics",
        "emoji": "📷",
        "description": "Canon DSLR digital camera"
    },
    {
        "id": 11,
        "title": "PlayStation 5",
        "price": 7800000,
        "location": "Tashkent",
        "category": "Gaming",
        "emoji": "🎮",
        "description": "Sony PlayStation 5 console"
    },
    {
        "id": 12,
        "title": "Xbox Series X",
        "price": 6500000,
        "location": "Samarkand",
        "category": "Gaming",
        "emoji": "🎮",
        "description": "Microsoft Xbox Series X"
    },
    {
        "id": 13,
        "title": "LG Smart TV 55",
        "price": 6800000,
        "location": "Tashkent",
        "category": "Electronics",
        "emoji": "📺",
        "description": "55-inch LG Smart television"
    },
    {
        "id": 14,
        "title": "Dyson Vacuum Cleaner",
        "price": 5500000,
        "location": "Namangan",
        "category": "Home",
        "emoji": "🧹",
        "description": "Dyson cordless vacuum cleaner"
    },
    {
        "id": 15,
        "title": "Coffee Machine",
        "price": 2100000,
        "location": "Tashkent",
        "category": "Home",
        "emoji": "☕",
        "description": "Automatic coffee machine"
    },
    {
        "id": 16,
        "title": "Gaming Chair",
        "price": 1800000,
        "location": "Fergana",
        "category": "Furniture",
        "emoji": "🪑",
        "description": "Comfortable ergonomic gaming chair"
    },
    {
        "id": 17,
        "title": "Office Desk",
        "price": 1300000,
        "location": "Tashkent",
        "category": "Furniture",
        "emoji": "🪵",
        "description": "Modern wooden office desk"
    },
    {
        "id": 18,
        "title": "Xiaomi Power Bank",
        "price": 250000,
        "location": "Andijan",
        "category": "Accessories",
        "emoji": "🔋",
        "description": "20000mAh portable power bank"
    },
    {
        "id": 19,
        "title": "Samsung Galaxy Tab S9",
        "price": 6200000,
        "location": "Tashkent",
        "category": "Electronics",
        "emoji": "📱",
        "description": "Samsung Galaxy Tab S9 tablet"
    },
    {
        "id": 20,
        "title": "JBL Flip 6",
        "price": 1100000,
        "location": "Samarkand",
        "category": "Accessories",
        "emoji": "🔊",
        "description": "Portable Bluetooth speaker"
    }
]


@app.get("/")
def home():
    return {
        "message": "Marketly API is running",
        "total_products": len(products)
    }


@app.get("/api/products")
def get_products(
    search: str = "",
    category: str = ""
):
    result = products

    if search:
        result = [
            p for p in result
            if search.lower() in p["title"].lower()
        ]

    if category and category != "All":
        result = [
            p for p in result
            if p["category"] == category
        ]

    return result


@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}
