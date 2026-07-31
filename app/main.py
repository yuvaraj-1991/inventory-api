from fastapi import FastAPI

app = FastAPI(
    title="Inventory API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Inventory API"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/products")
def products():
    return {
        "products": [
            {
                "id": 1,
                "name": "Laptop",
                "quantity": 25
            },
            {
                "id": 2,
                "name": "Keyboard",
                "quantity": 100
            },
            {
                "id": 3,
                "name": "Mouse",
                "quantity": 75
            }
        ]
    }