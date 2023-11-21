from typing import Optional

from pydantic import BaseModel


class CreateAdverts(BaseModel):
    title: str
    description: str
    owner: str


class UpdateAdverts(BaseModel):
    title: Optional[str]
    description: Optional[str]
    owner: Optional[str]