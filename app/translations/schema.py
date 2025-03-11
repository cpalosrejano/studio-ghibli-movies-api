from typing import Optional

from pydantic import BaseModel

class MovieTranslation(BaseModel):
    title: Optional[str] = None
    description: str