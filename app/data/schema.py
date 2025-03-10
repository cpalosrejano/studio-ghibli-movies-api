from pydantic import BaseModel


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