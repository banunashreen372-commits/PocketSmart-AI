import os

try:
    from dotenv import load_dotenv  # type: ignore[reportMissingImports]
except ImportError:
    def load_dotenv():
        """Allow configuration to work when python-dotenv is unavailable."""
        return False

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "pocketsmart-secret-key")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-1.5-flash"
    )

    UPLOAD_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "uploads"
    )

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024