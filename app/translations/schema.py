from pydantic import BaseModel

class MovieTranslation(BaseModel):
    title: str
    description: str