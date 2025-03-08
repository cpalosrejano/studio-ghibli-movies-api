from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Datos en memoria
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

# Endpoint to check the abailability of API
@app.get("/ping")
def ping():
    return {"ping": datetime.now().isoformat()}
