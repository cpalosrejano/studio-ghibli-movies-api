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
def get_movies(
        lang: str = Query("en", description="Language in which you will receive the data. By default is English."),
        coproductions: bool = Query(False, description="includes movies that were co-produced by Studio Ghibli")):

    # get all movies
    return get_all_movies(lang, coproductions)



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
    release_date: int
    running_time: int
    rt_score: int
    coproduction: bool

def get_all_movies(lang: str, include_coproductions: bool) -> List[Movie]:

    # load translator in the desired language
    _ = get_translator(lang).gettext

    movies = [
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
            release_date=1984,
            running_time=116,
            rt_score=91,
            coproduction = False
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
            release_date=1986,
            running_time=124,
            rt_score=96,
            coproduction = False
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
            release_date=1988,
            running_time=93,
            rt_score=100,
            coproduction = False
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
            release_date=1988,
            running_time=86,
            rt_score=94,
            coproduction = False
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
            release_date=1989,
            running_time=101,
            rt_score=98,
            coproduction = False
        ),
        Movie(
            id="b79c22e7-a35e-44f8-a01d-786928ac9761",
            title="Only Yesterday",
            description="Only Yesterday revolves around Taeko, a single woman working a desk job in Tokyo in 1982, taking a vacation in the countryside with the family of her sister in-law. During her vacation, Taeko finds herself looking back at her time as a young schoolgirl growing up in 1966. The film flips back and forth between the two time periods with a lot of nostalgia and beautiful country scenery as Taeko sorts out her flashbacks and tries to make some tough decisions about her future.",
            title_romanised="Omohide Poro Poro",
            image_cartel="https://resizing.flixster.com/AhWAif9MU5TIoe8QD0KsxRi_4go=/fit-in/705x460/v2/https://resizing.flixster.com/GMXOIc2qji2sLUuSxsvngLTkb3M=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2JlNWVkYTQ2LWVjN2EtNDE0ZS1hZjkzLTcxNzFmNzJhMTc3YS53ZWJw",
            image_banner="https://resizing.flixster.com/-yAst9h9BfApu7UkKEfr01650bg=/fit-in/705x460/v2/https://resizing.flixster.com/3VGRBUenNni8029YCcGYsWyvStM=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzBmZDJjOWI3LTBiYzItNDVjYy04MDEyLTAzNGJhNzJiMzc4MS53ZWJw",
            director="Isao Takahata",
            producer="Hayao Miyazaki, Toshio Susuki, Yasuyoshi Tokuma, Yoshio Sasaki, Ritsuo Isobe",
            soundtrack="Masaru Hoshi",
            release_date=1991,
            running_time=118,
            rt_score=100,
            coproduction = False
        ),
        Movie(
            id="ea4c45df-bd15-4ef0-83f9-f6f9dca675cb",
            title="Porco Rosso",
            description="In Early 1930's era Italy, air pirates, bounty hunters and high flyers of all sorts rule the skies. The most cunning and skilled of these pilots is Porco Rosso, a man cursed with the head of a pig after watching the spirits of the pilots killed in the last air battle he fought in rise to the heavens. He now makes a living taking jobs, such as rescuing those kidnapped by air pirates. Donald Curtis, Porco's rival in the air and in catching the affections of women, provides a constant challenge to the hero, culminating in a hilarious, action packed finale.",
            title_romanised="Kurenai no buta",
            image_cartel="https://resizing.flixster.com/B_5NwogQmCjMh-3GSZIHf-19ySk=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p160147_p_v8_ac.jpg",
            image_banner="https://resizing.flixster.com/nMfGpB37NFsCG97Jr0zmFXtoGyE=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/82008_ba.jpg",
            director="Hayao Miyazaki",
            producer="Toshio Suzuki",
            soundtrack="Joe Hisaishi",
            release_date=1992,
            running_time=94,
            rt_score=96,
            coproduction = False
        ),
        Movie(
            id="1fe5ba48-40ad-4059-ba8f-37ee9ff4d8c4",
            title="Ocean Waves",
            description="The main character travels to his hometown for his high school reunion. During the trip, he recalls the memories of the days in high school. Friendship, subtle love, a trip to Tokyo and so on all came back to him as the film evolves.",
            title_romanised="Umi ga kikoeru",
            image_cartel="https://resizing.flixster.com/2TL-KGDgtjPkMiESKwCq_Yrdvkg=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p8477698_v_v8_ad.jpg",
            image_banner="https://resizing.flixster.com/tQzIAhqVovYBRdckGrtCiGX804g=/fit-in/705x460/v2/https://resizing.flixster.com/8P2iU5EuSGQX1J-S77ukFyo5pw8=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzE3NmZmMDhmLWU2M2QtNDVlYi1hMmU1LWIxYTlhYWZlZDQ4NC53ZWJw",
            director="Tomomi Mochizuki",
            producer="Nozomu Takahashi, Toshio Suzuki, Seiji Okuda",
            soundtrack="Shigeru Nagata",
            release_date=1993,
            running_time=72,
            rt_score=89,
            coproduction = False
        ),
        Movie(
            id="caca9a5a-6e05-47df-9ef0-de57508ecea9",
            title="Pom Poko",
            description="As the human city development encroaches on the raccoon population's forest and meadow habitat, the raccoons find themselves faced with the very real possibility of extinction. In response, the raccoons engage in a desperate struggle to stop the construction and preserve their home.",
            title_romanised="Heisei Tanuki Gassen Ponpoko",
            image_cartel="https://resizing.flixster.com/TXvyfbacStvaXZDIYkOscIbWJBg=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p24121_p_v8_ad.jpg",
            image_banner="https://resizing.flixster.com/-dxE5pVqANoWz3jqbuSOP2Wq7dc=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p24121_i_h10_ac.jpg",
            director="Isao Takahata",
            producer="Toshio Suzuki, Hayao Miyazaki",
            soundtrack="Chang Chang Typhoon",
            release_date=1994,
            running_time=119,
            rt_score=86,
            coproduction = False
        ),
        Movie(
            id="07b21060-7236-4939-a414-d9c3b868eefe",
            title="Whisper of the Heart",
            description="A young girl finds that all the books she chooses in the library have been previously checked out by the same boy. Later she meets a very infuriating fellow... could it be her \"friend\" from the library? The boy's grandfather has a violin sales and service shop. The boy wants to be a violin maker like his grandfather.",
            title_romanised="Mimi wo sumaseba",
            image_cartel="https://resizing.flixster.com/yXm0ME9MxTd04enCKbhkcUISs4g=/fit-in/705x460/v2/https://resizing.flixster.com/iOYqoVyKuD1A_JnUrUlTE6BkCeM=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2VjMGM0MDRjLWZlMDItNGU5OS05MzIzLTMxZjczYTNmYmI3Yi5qcGc=",
            image_banner="https://resizing.flixster.com/97pmKEMrKYHXAEnNk5SDu9B_cEI=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p160148_i_h11_ab.jpg",
            director="Yoshifumi Kondô",
            producer="Toshio Suzuki, Yasuyoshi Tokuma",
            soundtrack="Yuji Nomi",
            release_date=1995,
            running_time=111,
            rt_score=95,
            coproduction = False
        ),
        Movie(
            id="329b6ac9-b6cc-426d-bf20-4deff5be1f5f",
            title="Princess Mononoke",
            description="A prince is infected with an incurable disease by a possessed boar/god. He is to die unless he can find a cure to rid the curse from his body. It seems that his only hope is to travel to the far east. When he arrives to get help from the deer god, he finds himself in the middle of a battle between the animal inhabitants of the forest and an iron mining town that is exploiting and killing the forest. Leading the forest animals in the battle is a human raised by wolves, Princess Mononoke.",
            title_romanised="Mononoke-hime",
            image_cartel="https://resizing.flixster.com/mv1ttpDFqM1EC0iIRO-PoEQUX5s=/fit-in/705x460/v2/https://resizing.flixster.com/fLUbEbfgnDvNc1kHMC62jFcMny0=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2QxM2YyODA1LThhYWItNGU4Zi1iMjk3LTg4YmZhMGE3ZTQwMy5qcGc=",
            image_banner="https://resizing.flixster.com/Uh3LSoauJYH1R1qGK3i8TGRU7zw=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p23052_i_h10_aa.jpg",
            director="Hayao Miyazaki",
            producer="Toshio Suzuki",
            soundtrack="Joe Hisaishi",
            release_date=1997,
            running_time=133,
            rt_score=93,
            coproduction = False
        ),
        Movie(
            id="953623e1-82ca-4077-965d-61a2fdfef4e2",
            title="My Neighbors the Yamadas",
            description="The Yamadas are a typical middle class Japanese family in urban Tokyo and this film shows us a variety of episodes of their lives. With tales that range from the humourous to the heartbreaking, we see this family cope with life's little conflicts, problems and joys in their own way.",
            title_romanised="Hôhokekyo Tonari no Yamada-kun",
            image_cartel="https://resizing.flixster.com/30zpuxRZVatF05gk7rXFY3L21fM=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p10098132_v_v8_ab.jpg",
            image_banner="https://resizing.flixster.com/iePob_UQrVPWDQ6DByYNL9MGnbI=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p10098132_i_h9_ab.jpg",
            director="Isao Takahata",
            producer="Toshio Suzuki, Isao Takahata, Takashi Shoji, Yasuyoshi Tokuma, Seiichirô Ujiie",
            soundtrack="Akiko Yano",
            release_date=1999,
            running_time=104,
            rt_score=78,
            coproduction = False
        ),
        Movie(
            id="2f2613ef-b2a0-45f0-8c33-86df05f23c32",
            title="Spirited Away",
            description="10-year old Chihiro becomes trapped in a forbidden world of gods and magic when her parents take her to investigate the other side of the tunnel. In order to survive, Chihiro must work and make herself useful, and find within her the courage and resolve she needs to save her parents and escape from a world where humans are dispised.",
            title_romanised="Sen to Chihiro no kamikakushi",
            image_cartel="https://resizing.flixster.com/teUSXAaRN7f0vdqI_GZeqagzkos=/fit-in/705x460/v2/https://resizing.flixster.com/toMzSC_5b1NF7MxJ5-CJeL1S-Z8=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzRlY2RiZDcyLWU5ZmEtNDliMy1iOTMyLTYzNzhjY2RjOWIxNy5qcGc=",
            image_banner="https://resizing.flixster.com/NxW5It1T327OCk6B4-xOQzOcitM=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/32913_ac.jpg",
            director="Hayao Miyazaki",
            producer="Toshio Susuki",
            soundtrack="Joe Hisaishi",
            release_date=2001,
            running_time=124,
            rt_score=96,
            coproduction = False
        ),
        Movie(
            id="bb8a5c3d-0db2-47bc-89c7-2331d803d067",
            title="The Cat Returns",
            description="Haru is a young girl who rescues a mysterious cat from traffic and soon finds herself the unwelcome recipient of gifts and favors from the King of the Cats, who also wants her to marry his son, Prince Lune.",
            title_romanised="Neko no ongaeshi",
            image_cartel="https://resizing.flixster.com/fRU5WRP-tB7MZ4e3STAd4Y8JNMs=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/NowShowing/120446/120446_aa.jpg",
            image_banner="https://resizing.flixster.com/NKJZug28C8Fnd8KuiXp_47YLz1A=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/120446_be.jpg",
            director="Hiroyuki Morita",
            producer="Toshio Suzuki, Nozomu Takahashi",
            soundtrack="Yuji Nomi",
            release_date=2002,
            running_time=75,
            rt_score=88,
            coproduction = False
        ),
        Movie(
            id="04fc5ab9-2cf0-4aad-b56c-a4d9423556af",
            title="Howl's Moving Castle",
            description="Young Sophie is eighteen, and works tirelessly every day making hats in her deased father’s hat shop. One day, on a rare outing to town, Sophie accidentally encounters the Wizard Howl. Howl is dashingly handsome, yet as wizards go, he’s a bit of a wimp. The Witch of the Waste misinterprets the nature of the relationship between the two and casts a spell on Sophie, transforming her into a withered ninety-year-old woman. Sophie leaves home and wanders in the wasteland, where she enters Howl’s moving castle by chance. Hiding her true identity, she settles in as Howl’s live-in cleaning lady. Feisty old Sophie shakes the house up, with much more pep than she had as her original younger self. What will Sophie do, and what will happen between her and Howl?",
            title_romanised="Hauru no Ugoku Shiro",
            image_cartel="https://resizing.flixster.com/5MzJJLj-uhEv1FgWtuRAtm3OJT0=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p36095_p_v8_ae.jpg",
            image_banner="https://resizing.flixster.com/65X-bpKVnpGcwIQkFl0IOkWKcY8=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/46617_bb.jpg",
            director="Hayao Miyazaki",
            producer="Hayao Miyazaki, Toshio Suzuki, Tomohiko Ishii",
            soundtrack="Joe Hisaishi",
            release_date=2004,
            running_time=109,
            rt_score=95,
            coproduction = False
        ),
        Movie(
            id="cee3bde0-3635-4ecf-9731-9655737795f7",
            title="Tales from Earthsea",
            description="Something bizarre has come over the land. The kingdom is deteriorating. People are beginning to act strange... What's even more strange is that people are beginning to see dragons, which shouldn't enter the world of humans. Due to all these bizarre events, Ged, a wandering wizard, is investigating the cause. During his journey, he meets Prince Arren, a young distraught teenage boy. While Arren may look like a shy young teen, he has a severe dark side, which grants him strength, hatred, ruthlessness and has no mercy, especially when it comes to protecting Teru. For the witch Kumo this is a perfect opportunity. She can use the boy's \"fears\" against the very one who would help him, Ged.",
            title_romanised="Gedo Senki",
            image_cartel="https://resizing.flixster.com/z5RuyASkOeECi_X1MJK4_JLe_6c=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/NowShowing/92360/92360_aa.jpg",
            image_banner="https://resizing.flixster.com/EI6lYZf5VXOo-u-gxtJFUELF4bw=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p8126367_k_h10_aa.jpg",
            director="Goro Miyazaki",
            producer="Toshio Suzuki, Tomohiko Ishii",
            soundtrack="Tamiya Terashima, Carlos Núñez",
            release_date=2006,
            running_time=115,
            rt_score=46,
            coproduction = False
        ),
        Movie(
            id="451a4db6-8d9a-4499-b59f-60dc62d0bd27",
            title="Ponyo",
            description="During a forbidden excursion to see the surface world, a goldfish princess encounters a human boy named Sosuke, who gives her the name Ponyo. Ponyo longs to become human, and as her friendship with Sosuke grows, she becomes more humanlike. Ponyo's father brings her back to their ocean kingdom, but so strong is Ponyo's wish to live on the surface that she breaks free, and in the process, spills a collection of magical elixirs that endanger Sosuke's village.",
            title_romanised="Gake no ue no Ponyo",
            image_cartel="https://resizing.flixster.com/zIhx2bFuY_apdXqQS_NUhSm1Hns=/fit-in/705x460/v2/https://resizing.flixster.com/D_9DqMNrY1QERAtGKBvTx_6Mx9g=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzFkMGEwYzgyLTdjNWYtNGVlZi04NTkwLWQxNThhNDIzNmRlOS5qcGc=",
            image_banner="https://resizing.flixster.com/G_CYgH77BllgNQGdBYS2cOjbaDE=/fit-in/705x460/v2/https://resizing.flixster.com/WF8N0oOCUzjfQFDYg_LD5ScfSrk=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzA2ODllMDk2LWYwYmEtNGZjZi1hNGJkLTQ5MTY3MmNkYzg1Ny53ZWJw",
            director="Hayao Miyazaki",
            producer="Toshio Suzuki, Kōji Hoshino",
            soundtrack="Joe Hisaishi",
            release_date=2008,
            running_time=100,
            rt_score=91,
            coproduction = False
        ),
        Movie(
            id="e98c0fc1-1ccc-47d6-8e92-4a753f7f9253",
            title="The Secret World of Arrietty",
            description="Sho moves into his great aunt's house and soon discovers the presence of tiny people, the Borrowers, living there. A 14-year-old Borrower named Arrietty strives to prove herself by helping her father gather materials that her family needs from Sho's new home. However, Arrietty and Sho meet, breaking the rule that humans must not know about the Borrowers' existence. As Sho and Arrietty's relationship develops, human interference endangers the Borrowers' lives. Arrietty and Sho work together to try and protect the Borrowers' way of life.",
            title_romanised="Karigurashi no Arietti",
            image_cartel="https://resizing.flixster.com/YkUEbgj3eYf4EB4yExYBycxLvNY=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p8777609_p_v8_ae.jpg",
            image_banner="https://resizing.flixster.com/sb1pxSmo5RJrPfk4NHSq9p5TQ0w=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/109188_bg.jpg",
            director="Hiromasa Yonebayashi",
            producer="Toshio Suzuki, Koji Hoshino",
            soundtrack="Cécile Corbel",
            release_date=2010,
            running_time=94,
            rt_score=94,
            coproduction = False
        ),
        Movie(
            id="ef81985e-2b04-4e1b-8197-4c4c92b663e4",
            title="From Up on Poppy Hill",
            description="The story is set in 1963 in Yokohama. Kokuriko Manor sits on a hill overlooking the harbour. A 16 year-old girl, Umi, lives in that house. Every morning she raises a signal flag facing the sea. A 17 year-old boy, Shun, always sees this flag from the sea as he rides a tugboat to school. Gradually the pair are drawn to each other but they are faced with a sudden trial. Even so, they keep going without running from facing the hardships of reality.",
            title_romanised="Kokuriko-zaka kara",
            image_cartel="https://resizing.flixster.com/7illda2axOC_-9U4GVvOREvu0NE=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p8822358_v_v8_ab.jpg",
            image_banner="https://resizing.flixster.com/--UR5kAZwGbRpOD1bkVxLHVKqyw=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p8822358_i_h9_aa.jpg",
            director="Goro Miyazaki",
            producer="Toshio Suzuki, Tetsurō Sayama, Chizuru Takahashi",
            soundtrack="Satoshi Takebe",
            release_date=2011,
            running_time=91,
            rt_score=87,
            coproduction = False
        ),
        Movie(
            id="c45c90c9-38dc-435d-82a6-e6c06d03af26",
            title="The Wind rises",
            description="Jiro dreams of flying and designing beautiful airplanes, inspired by the famous Italian aeronautical designer Caproni. Nearsighted from a young age and unable to be a pilot, Jiro joins a major Japanese engineering company in 1927 and becomes one of the world's most innovative and accomplished airplane designers. The film chronicles much of his life, depicting key historical events, including the Great Kanto Earthquake of 1923, the Great Depression, the tuberculosis epidemic and Japan's plunge into war. Jiro meets and falls in love with Nahoko, and grows and cherishes his friendship with his colleague Honjo.",
            title_romanised="Kaze tachinu",
            image_cartel="https://resizing.flixster.com/NHnSUeqIPhbvPa2DgJq1mdx5VsE=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p10213771_v_v8_ab.jpg",
            image_banner="https://resizing.flixster.com/J1vuZDN2bGVj30stZwe7ocUR_yE=/fit-in/705x460/v2/https://resizing.flixster.com/C463WcdeN2zZ12Fwi0xg_vEWfGg=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2NhODc0OTRmLWFlYmYtNDc0Ny1hYjA5LTUwZDQ2NjVjMjc3MS53ZWJw",
            director="Hayao Miyazaki",
            producer="Toshio Suzuki",
            soundtrack="Joe Hisaishi",
            release_date=2013,
            running_time=125,
            rt_score=88,
            coproduction = False
        ),
        Movie(
            id="17be5479-9ec8-4e06-a313-d7d4b90d7eec",
            title="The Tale of Princess Kaguya",
            description="An old man makes a living by selling bamboo. One day, he finds a princess in a bamboo. The princess is only the size of a finger. Her name is Kaguya. When Kaguya grows up, 5 men from prestigious families propose to her. Kaguya asks the men to find memorable marriage gifts for her, but the 5 men are unable to find what Kaguya wants. Then, the Emperor of Japan proposes to her.",
            title_romanised="Kaguya-hime no Monogatari",
            image_cartel="https://resizing.flixster.com/kgUHxhKImjtefl5x4Z5EoXWONS8=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p10922577_p_v8_aa.jpg",
            image_banner="https://resizing.flixster.com/gy_RTYTV6N0USNZG1rZEUXe4H9M=/fit-in/705x460/v2/https://resizing.flixster.com/Tr0OTjtGlITCvZxWY021zy51MoE=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2JmYWVmOTNmLTQxOGEtNDdkZi1hODQxLTI4MmE1NzFiYjZlYy53ZWJw",
            director="Isao Takahata",
            producer="Yoshiaki Nishimura, Toshio Suzuki, Seiichirou Ujiie",
            soundtrack="Joe Hisaishi",
            release_date=2013,
            running_time=137,
            rt_score=100,
            coproduction = False
        ),
        Movie(
            id="edc0e537-aac8-42ec-8cc4-75e45551aa8e",
            title="When Marnie Was There",
            description="Anna hasn't a friend in the world - until she meets Marnie among the sand dunes. But Marnie isn't all she seems...An atmospheric ghost story with truths to tell about friendship, families and loneliness. Anna lives with foster parents, a misfit with no friends, always on the outside of things. Then she is sent to Norfolk to stay with old Mr and Mrs Pegg, where she runs wild on the sand dunes and around the water. There is a house, the Marsh House, which she feels she recognises - and she soon meets a strange little girl called Marnie, who becomes Anna's first ever friend. Then one day, Marnie vanishes. A new family, the Lindsays, move into the Marsh House. Having learnt so much from Marnie about friendship, Anna makes firm friends with the Lindsays - and learns some strange truths about Marnie, who was not all she seemed...",
            title_romanised="Omoide no Mânî",
            image_cartel="https://resizing.flixster.com/tXNHCDdg8LoPgcJdTymP-RUcHVU=/fit-in/705x460/v2/https://resizing.flixster.com/5ljZmB7n__vlOL3hAtwX9kLcm48=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzExZmIxZjFlLTM1YTctNDM5ZS04ZGNlLTc4YjkyYzkxMWFlNC5qcGc=",
            image_banner="https://resizing.flixster.com/Tq0rLgKQ2kh7fDf-89nutWuKBUg=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p11732407_i_h10_ab.jpg",
            director="Hiromasa Yonebayashi",
            producer="Toshio Suzuki, Yoshiaki Nishimura",
            soundtrack="Takatsugu Muramatsu",
            release_date=2014,
            running_time=103,
            rt_score=92,
            coproduction = False
        ),
        Movie(
            id="f16707a1-36de-4697-b751-eefd8200bf87",
            title="Earwig and the Witch",
            description="Not every orphan would love living at St. Morwald's Home for Children, but Earwig does. She gets whatever she wants, whenever she wants it, and it's been that way since she was dropped on the orphanage doorstep as a baby. But all that changes the day Bella Yaga and the Mandrake come to St. Morwald's, disguised as foster parents. Earwig is whisked off to their mysterious house full of invisible rooms, potions, and spell books, with magic around every corner. Most children would run in terror from a house like that . . . but not Earwig. Using her own cleverness—with a lot of help from a talking cat—she decides to show the witch who's boss.",
            title_romanised="Aya to Majo",
            image_cartel="https://resizing.flixster.com/mtQB_IB4WFwmDiaxESJTGfo1ncQ=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p19237363_k_v8_af.jpg",
            image_banner="https://resizing.flixster.com/6dC4YezDNj4Qs3V92SHPGe1DaJc=/fit-in/705x460/v2/https://resizing.flixster.com/K7-46rOe6fvLUkdHUKNx6_gfwHc=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzUzZjAzZGQyLWNmMWItNGI4MC1hNjZjLTQzYmU2Mzc2YTQ5Yi5qcGc=",
            director="Goro Miyazaki",
            producer="Toshio Suzuki",
            soundtrack="Satoshi Takebe",
            release_date=2020,
            running_time=82,
            rt_score=28,
            coproduction = False
        ),
        Movie(
            id="9144fb4f-83d2-4802-be7f-7f75d97cafc8",
            title="The Boy and the Heron",
            description="While the Second World War rages, the teenage Mahito, haunted by his mother's tragic death, is relocated from Tokyo to the serene rural home of his new stepmother Natsuko, a woman who bears a striking resemblance to the boy's mother. As he tries to adjust, this strange new world grows even stranger following the appearance of a persistent gray heron, who perplexes and bedevils Mahito, dubbing him the \"long-awaited one.\"",
            title_romanised="Kimitachi wa dô ikiru ka",
            image_cartel="https://resizing.flixster.com/x0LoaNH-06-Vtq1DMu4wyejzoPs=/fit-in/705x460/v2/https://resizing.flixster.com/Hk9p4GGqf6TNJ0f8TtJxTqjH5vA=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzU3MTE5MDA5LWY0MjEtNDgyYi04OThmLTU4NDNlYTFjZDk0NC5qcGc=",
            image_banner="https://resizing.flixster.com/J-qZNrQ6vUD4SoL8_ylOmta-DVA=/fit-in/705x460/v2/https://resizing.flixster.com/3Sjgo6MTYKyVjnjKaGXnLpMdX5E=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2MzNGMxYzUzLThmNWMtNDE2Ny04NWMzLWFkNzU3NTVkNzg2YS5qcGc=",
            director="Hayao Miyazaki",
            producer="Toshio Suzuki",
            soundtrack="Joe Hisaishi",
            release_date=2023,
            running_time=124,
            rt_score=96,
            coproduction = False
        )
    ]

    if include_coproductions:
        movies.append(
            Movie(
                id="8dcfe58e-1e58-4f68-9679-d10248fa13aa",
                title="The Red Turtle",
                description="The dialogue-less film follows the major life stages of a castaway on a deserted tropical island populated by turtles, crabs and birds.",
                title_romanised="La tortue rouge",
                image_cartel="https://resizing.flixster.com/WZfFKg3rl6IFUZnh_Bdteop-nq8=/206x305/v2/https://resizing.flixster.com/uw3zcrpSuW0nWDa-B7BnU99ZLzw=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzVkNzQxNDQ1LWE5Y2EtNDFjMC04NmU2LWY2ZWMwZmUwM2QxNS53ZWJw",
                image_banner="https://resizing.flixster.com/uXqGFFRvEOks5jJU6FANTEgqkY0=/fit-in/705x460/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/164637_bc.jpg",
                director="Michael Dudok de Wit",
                producer="Toshio Suzuki, Vincent Maraval, Pascal Caucheteux, Grégoire Sorlat, Léon Perahia",
                soundtrack="Laurent Perez del Mar",
                release_date=2016,
                running_time=80,
                rt_score=93,
                coproduction = True
            )
        )

    return movies

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

