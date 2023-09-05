from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Row:
    name: str
    measurement: str
    price: int
    diameter: str | None = None
    brand: str | None = None
    thickness: str | None = None
    shelf: str | None = None
    length: str | None = None
    size: str | None = None
    width: int | None = None
    wall: str | None = None
    dt: str = "now()"
