import logging

from fastapi import FastAPI

from app.classifier import classify_request
from app.config import settings
from app.logging_config import configure_logging
from app.middleware.request_logging import log_requests
from app.schemas import ClassificationRequest, ClassificationResponse

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.middleware("http")(log_requests)

logger.info(
    "Application started | environment=%s | version=%s",
    settings.environment.value,
    settings.app_version,
)


@app.get("/")
def read_root():
    return {"message": f"{settings.app_name} is running"}


@app.post("/classify", response_model=ClassificationResponse)
def classify_endpoint(
    request: ClassificationRequest,
) -> ClassificationResponse:
    result = classify_request(request.text)

    return ClassificationResponse(
        category=result.category,
        priority=result.priority,
        normalized_text=request.text,
    )


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "version": settings.app_version,
        "environment": settings.environment,
    }
