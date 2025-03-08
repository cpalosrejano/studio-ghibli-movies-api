from fastapi import FastAPI, Query
from datetime import datetime
from fastapi.responses import HTMLResponse

# for get_all_movies and Movie class
from pydantic import BaseModel
from typing import List

# translations
import gettext
import os

############################################################
## start of api
############################################################


app = FastAPI()

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

@app.get("/ping")
def ping():
    return {"ping": datetime.now().isoformat()}

@app.get("/movies")
def get_movies(lang: str = Query("en", description="Language in which you will receive the data. By default is English.")):
    print("Language desired is " + lang)
    return get_all_movies(lang)

############################################################
## end of api
############################################################




############################################################
## start of Movie and get_all_movies
############################################################

class Movie(BaseModel):
    id: str
    title: str
    title_romanised: str
    image_cartel: str
    image_banner: str
    description: str
    director: str
    producer: str
    soundtrack: str
    release_date: str
    running_time: str
    rt_score: str

def get_all_movies(lang: str) -> List[Movie]:

    # load translator in the desired language
    _ = get_translator(lang).gettext

    return [
        Movie(
            id="47d71eb5-a93f-43fe-b51d-6563cd0bd8b4",
            title="Nausicaä of the Valley of the Wind",
            description="Far in the future, after an apocalyptic conflict has devastated much of the world's ecosystem, the few surviving humans live in scattered semi-hospitable environments within what has become a \"toxic jungle.\" Young Nausicaä lives in the arid Valley of the Wind and can communicate with the massive insects that populate the dangerous jungle. Under the guidance of the pensive veteran warrior, Lord Yupa, Nausicaä works to bring peace back to the ravaged planet.",
            title_romanised="Kaze no Tani no Naushikaaka",
            image_cartel="https://resizing.flixster.com/M-rKJnoNR9EZdvs45q07-F-5KYY=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p160143_p_v8_ad.jpg",
            image_banner="https://resizing.flixster.com/ULgIqcCj0sLc27OGw54OJ41dsiY=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p160143_i_h10_ab.jpg",
            director="Hayao Miyazaki",
            producer="Hakuhodo, Nibariki, Tokuma Shoten, Topcraft",
            soundtrack="Joe Hisaishi",
            release_date="1984",
            running_time="116",
            rt_score="91"
        ),
        Movie(
            id="6baffca4-7881-413f-9d8a-a9137de942bb",
            title="Castle in the Sky",
            description="Laputa, a floating castle in the sky, was created by a mysterious race of people who long ago disappeared from the planet. A group of ruthless pirates suspect it has treasures and riches beyond imagination. The government wants to find out if it holds the power to rule the world. Both are chasing a girl named Sheeta in their quest for this hidden city because only the secret spells passed down to Sheeta by her grandmother can unlock the puzzle.",
            title_romanised="Tenkû no Shiro Rapyutaaka",
            image_cartel="https://resizing.flixster.com/FtzWuqQu-2R8gdLYbsFYs73yRaI=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p68228_p_v8_aa.jpg",
            image_banner="https://resizing.flixster.com/M75tbdJk9S_eykxSQ29a51_SSjQ=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p68228_i_h11_aa.jpg",
            director="Hayao Miyazaki",
            producer="Isao Takahata",
            soundtrack="Joe Hisaishi",
            release_date="1986",
            running_time="124",
            rt_score="96"
        ),
        Movie(
            id="55d79b98-58a7-4438-9d25-e99e8e088a4e",
            title="Grave of Fireflies",
            description="A Japanese boy of 14 and his 4 year old sister, attempt to seek refuge from the atrocities of World War II in the small city of Kobe. In post-World War II Japan, a janitor finds a metal sweet container beside a deathly ill boy. The janitor tosses the canister into the night, unwittingly beginning a most unusual tale of survival amid war. Brother and sister Seita and Setsuko, flee their disheveled home and deceased parents to make their bid for a new life. Before American troops begin to occupy their country, the children resort to dwelling in an abandoned bomb shelter in the countryside. Though these siblings later get a sense of safety, they realize necessities such as food and water will not be easy to come by.",
            title_romanised="Hotaru no Haka",
            image_cartel="https://resizing.flixster.com/eO24tGQFT7R9V6r0PwjRanUG7wA=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p158931_i_v9_aa.jpg",
            image_banner="https://resizing.flixster.com/OubaPxkxkhhQHRWVRuaGZIpg370=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p158931_i_h9_aa.jpg",
            director="Isao Takahata",
            producer="Toru Hara",
            soundtrack="Michio Mamiya",
            release_date="1988",
            running_time="93",
            rt_score="100"
        ),
        Movie(
            id="12710c0b-b598-400b-a4b9-dba03c8c1dc7",
            title="My Neighbor Totoro",
            description="Two young girls, Satsuke and her younger sister Mei, move into a house in the country with their father to be closer to their hospitalized mother. Satsuke and Mei discover that the nearby forest is inhabited by magical creatures called Totoros (pronounced toe-toe-ro). They soon befriend these Totoros, and have several magical adventures.",
            title_romanised="Tonari no Totoro",
            image_cartel="https://resizing.flixster.com/K-PU3Tc3HDXsouWJ-T5wtl4KkAI=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p160146_v_v8_ac.jpg",
            image_banner="https://resizing.flixster.com/bFcP8E8hGnhiolanoQehGeUEAZU=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p160146_i_h10_aa.jpg",
            director="Hayao Miyazaki",
            producer="Isao Takahata, Toshio Suzuki, Toru Hara",
            soundtrack="Joe Hisaishi",
            release_date="1988",
            running_time="86",
            rt_score="94"
        ),
        Movie(
            id="7dc4c683-7c34-4243-b940-77d411db3aa2",
            title="Kiki's Delivery Service",
            description="Kiki, a young witch-in-training, has reached the age of 13. According to tradition, all witches of that age must leave home for one year, so that they can learn how to live on their own. Kiki, along with her talking cat Gigi, fly away to live in the seaside town of Korico. After starting her own delivery service (using her broom as the delivery vehicle), Kiki must learn how to deal with her new life, especially after she loses the power to fly.",
            title_romanised="Majo no takkyûbin",
            image_cartel="https://resizing.flixster.com/IrCGjJEtmY39j2Zg7bS1j1WUYqk=/fit-in/705x460/v2/https://resizing.flixster.com/m_N-FYC2WS9IhDoWZqPHap_3YPA=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2ZmN2U1NGQzLTFmYzctNGJmNi04ZjI5LWEwMzU3MjE2NGQ5Yy5qcGc=",
            image_banner="https://resizing.flixster.com/KRi8GoeLB62ELSsCagTWRJVKZLs=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/11626_ba.jpg",
            director="Hayao Miyazaki",
            producer="Hayao Miyazaki, Toru Hara",
            soundtrack="Joe Hisaishi",
            release_date="1989",
            running_time="101",
            rt_score="98"
        ),
        Movie(
            id="",
            title="",
            description="",
            title_romanised="",
            image_cartel="",
            image_banner="",
            director="",
            producer="",
            soundtrack="",
            release_date="",
            running_time="",
            rt_score=""
        ),
    ]

### 1. Nausicaä of the Valley of the Wind (https://www.filmaffinity.com/es/film313630.html)
### 2. El castillo en el cielo (https://www.filmaffinity.com/es/film360886.html)
### 3. La tumba de luciérnagas (https://www.filmaffinity.com/es/film582716.html)
### 4. Mi vecino Totoro (https://www.filmaffinity.com/es/film646631.html)
### 5. Kiki: Entregas a domicilio (https://www.filmaffinity.com/es/film583615.html)
# 6. Recuerdos del ayer (https://www.filmaffinity.com/es/film235776.html)
# 7. Porco Rosso (https://www.filmaffinity.com/es/film169128.html)
# 8. Puedo escuchar el mar (https://www.filmaffinity.com/es/film747473.html)
# 9. Pompoko (https://www.filmaffinity.com/es/film622966.html)
# 10. Susurros del corazón (https://www.filmaffinity.com/es/film920920.html)
# 11. La princesa Mononoke (https://www.filmaffinity.com/es/film890814.html)
# 12. Mis vecinos los Yamada (https://www.filmaffinity.com/es/film348798.html)
# 13. El viaje de Chihiro (https://www.filmaffinity.com/es/film759533.html)
# 14. Haru en el reino de los gatos (https://www.filmaffinity.com/es/film520479.html)
# 15. El castillo ambulante (https://www.filmaffinity.com/es/film191978.html)
# 16. Cuentos de Terramar (https://www.filmaffinity.com/es/film449251.html)
# 17. Ponyo en el acantilado (https://www.filmaffinity.com/es/film576841.html)
# 18. Arriety y el mund de los diminutos (https://www.filmaffinity.com/es/film137389.html)
# 19. La colina de las amapolas (https://www.filmaffinity.com/es/film213523.html)
# 20. El viento se levanta (https://www.filmaffinity.com/es/film835261.html)
# 21. El cuento de la princesa Kaguya (https://www.filmaffinity.com/es/film931294.html)
# 22. El recuerdo de Marnie (https://www.filmaffinity.com/es/film576456.html)
# 23. Earwig y la bruja (https://www.filmaffinity.com/es/film836225.html)
# 24. El niño y la garza (https://www.filmaffinity.com/es/film489419.html)
# 25. Extra: La tortuga roja (https://www.filmaffinity.com/es/film932838.html)
# 26. Extra: Ghost in the shell 2: Innocence (https://www.filmaffinity.com/es/film958327.html)

############################################################
## end of Movie and get_all_movies
############################################################



############################################################
## START of TRANSLATOR
############################################################

# function to fetch the translator
def get_translator(lang: str):
    lang_path = "translations/" + lang + "/LC_MESSAGES/messages.mo"

    if os.path.exists(lang_path):  # if lang exist in translations folders, use it
        return gettext.translation("messages", localedir="translations", languages=[lang])

    # if lang does not exist in translations folder, use en by default
    return gettext.translation("messages", localedir="translations", languages=["en"])

