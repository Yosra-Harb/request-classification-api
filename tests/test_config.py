import pytest
from pydantic import ValidationError

from app.config import Settings
from app.enums import Environment, LogLevel

def test_settings_use_default_values():
    settings = Settings(_env_file=None)

    assert settings.environment == Environment.DEVELOPMENT
    assert settings.log_level == LogLevel.INFO


def test_settings_accept_valid_environment():
    settings = Settings(
        environment="production",
    )

    assert settings.environment == Environment.PRODUCTION


def test_settings_reject_invalid_environment():
    with pytest.raises(ValidationError):
        Settings(
            environment="banana",
        )


def test_settings_accept_valid_log_level():
    settings = Settings(
        log_level="DEBUG",
    )

    assert settings.log_level == LogLevel.DEBUG


def test_settings_reject_invalid_log_level():
    with pytest.raises(ValidationError):
        Settings(
            log_level="LOUD",
        )