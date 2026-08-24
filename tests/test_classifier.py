from app.classifier import classify_request
from app.enums import Category, Priority


def test_classifies_technical_request():
    result = classify_request("I cannot login to my account")

    assert result.category == Category.TECHNICAL
    assert result.priority == Priority.NORMAL


def test_classifies_financial_request():
    result = classify_request("I have a payment problem")

    assert result.category == Category.FINANCIAL
    assert result.priority == Priority.HIGH


def test_classifies_administrative_request():
    result = classify_request("I need a document")

    assert result.category == Category.ADMINISTRATIVE
    assert result.priority == Priority.NORMAL


def test_classifies_general_request():
    result = classify_request("I would like more details")

    assert result.category == Category.GENERAL
    assert result.priority == Priority.LOW


def test_does_not_match_keyword_inside_another_word():
    result = classify_request("I need more information")

    assert result.category == Category.GENERAL
    assert result.priority == Priority.LOW


def test_classification_is_case_insensitive():
    result = classify_request("I CANNOT LOGIN")

    assert result.category == Category.TECHNICAL
    assert result.priority == Priority.NORMAL
