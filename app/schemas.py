from pydantic import BaseModel, Field, field_validator

from app.enums import Category, Priority, RequestSource


class ClassificationRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Text of the request to classify",
    )

    source: RequestSource = RequestSource.WEB

    @field_validator("text", mode="before")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        if isinstance(value, str):
            return value.strip()

        return value


class ClassificationResponse(BaseModel):
    category: Category
    priority: Priority
    normalized_text: str


class ClassificationResult(BaseModel):
    category: Category
    priority: Priority