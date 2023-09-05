from datetime import date

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    measurement: str
    price: int
    diameter: str | None
    brand: str | None
    thickness: str | None
    shelf: str | None
    length: str | None
    size: str | None
    width: int | None
    wall: str | None
    dt: date
