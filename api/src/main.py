from api.v1 import recent
from config import APISettings
from fastapi import FastAPI
from fastapi_pagination import add_pagination

app = FastAPI(
    title=APISettings().project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)

add_pagination(app)
app.include_router(recent.router, prefix="/api/v1/recent", tags=["recent"])
