from http import HTTPStatus

from database import get_recent_parsing
from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from models import Item

router = APIRouter()


@router.get(
    "/",
    response_model=Page[Item],
    summary="Returns latest paginated parsing results.",
    response_description="Paginated parsing results.",
)
async def films_index() -> Page[Item]:
    items = get_recent_parsing()
    if not items:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="No items found.")
    response = [Item(**x.__dict__) for x in items]
    return paginate(response)
