from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.app.api.health import router as health_router
from backend.app.core.config import get_settings

PROJECT_ROOT = Path(__file__).resolve().parents[2]
templates = Jinja2Templates(directory=PROJECT_ROOT / "frontend" / "templates")


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        docs_url="/api/docs" if settings.app_env != "production" else None,
        redoc_url=None,
    )
    application.mount(
        "/static",
        StaticFiles(directory=PROJECT_ROOT / "frontend" / "static"),
        name="static",
    )
    application.include_router(health_router)

    @application.get("/", include_in_schema=False)
    async def home(request: Request):
        return templates.TemplateResponse(
            request=request,
            name="home.html",
            context={"app_name": settings.app_name},
        )

    return application


app = create_app()
