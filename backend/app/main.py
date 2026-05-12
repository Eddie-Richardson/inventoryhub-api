from fastapi import FastAPI
from backend.app.routers.products import router # Import the router from products.py

app = FastAPI(title="InventoryHub API")

# Include the router
app.include_router(router, prefix="/products", tags=["Products"])

@app.get("/health")
def health_check():
    return {"status": "ok"}