import re

from app.enums import Category, Priority
from app.schemas import ClassificationResult


def contains_keyword(text: str, keyword: str) -> bool:
    pattern = rf"\b{re.escape(keyword)}\b"
    return re.search(pattern, text) is not None


def classify_request(text: str) -> ClassificationResult:
    normalized_text = text.lower()

    if contains_keyword(normalized_text, "password") or contains_keyword(
        normalized_text, "login"
    ):
        category = Category.TECHNICAL
        priority = Priority.NORMAL

    elif contains_keyword(normalized_text, "invoice") or contains_keyword(
        normalized_text, "payment"
    ):
        category = Category.FINANCIAL
        priority = Priority.HIGH

    elif contains_keyword(normalized_text, "form") or contains_keyword(
        normalized_text, "document"
    ):
        category = Category.ADMINISTRATIVE
        priority = Priority.NORMAL

    else:
        category = Category.GENERAL
        priority = Priority.LOW

    return ClassificationResult(
        category=category,
        priority=priority,
    )
