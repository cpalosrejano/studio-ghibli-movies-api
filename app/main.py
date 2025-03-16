from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from app.data.movie.repository import get as get_movies_from_repository
from app.translations.translator import translate_movies

############################################################
## start of api
############################################################


app = FastAPI(
    title="Studio Ghibli Movies API",
    description="API which provices a basic but detailed information about all movies from Studio Ghibli",
    version="1.0.0",
    contact={
        "name": "Cristian",
        "email": "cpalosrejano@gmail.com",
    }
)

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

@app.get("/movies",
         summary="Get movies",
         description="This endpoint return a complete list of Studio Ghibli movies")
def get_movies(
        locale: str = Query("en", description="Language in which the API will return data. Format en-UK"),
        coproductions: bool = Query(False, description="Includes films that have been co-produced by by Studio Ghibli")):

    # get movies (with or without coproductions)
    movies = get_movies_from_repository(coproductions)

    # for now we get only the laguage, not the variant
    locale = locale.strip().lower()
    lang = locale.split("-")[0] if "-" in locale else locale

    # translate movies to custom lang
    movies_translated = translate_movies(movies, lang)

    return movies_translated
