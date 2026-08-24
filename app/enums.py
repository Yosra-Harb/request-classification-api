from enum import Enum

class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"

class LogLevel(str, Enum):
     DEBUG = "DEBUG"
     INFO = "INFO"
     WARNING = "WARNING"
     ERROR = "ERROR"
     CRITICAL = "CRITICAL" 

class RequestSource(str, Enum):
    WEB = "web"
    MOBILE = "mobile"
    EMAIL = "email"
    INTERNAL = "internal"


class Category(str, Enum):
    TECHNICAL = "technical"
    FINANCIAL = "financial"
    ADMINISTRATIVE = "administrative"
    GENERAL = "general"


class Priority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
