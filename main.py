from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import HTMLResponse

app = FastAPI()

# Datos en memoria
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

# Endpoint to check the abailability of API
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def root():
    return """
    <html>
        <head>
            <title>Studio Ghibli Movies API</title>
        </head>
        <body>
            <h1>Welcome to Studio Ghibli Movies API</h1>
            <h4>An open source and free API to fetch every studio ghibli movie detail</h4>

            <h3>Endpoints specifications:</h3>
            <ul>
                <li><a href="/docs" target="_blank">Swagger UI</a></li>
                <li><a href="/redoc" target="_blank">ReDoc</a></li>
            </ul>

            <h3>Source code:</h3>
            <p>You can found the source code in <a href="https://github.com/cpalosrejano/studio-ghibli-movies-api" target="_blank">Github</a></p>
        </body>
    </html>
    """

# Endpoint to check the abailability of API
@app.get("/ping")
def ping():
    return {"ping": datetime.now().isoformat()}
