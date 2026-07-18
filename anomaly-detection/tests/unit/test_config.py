from app.core.config import settings


def test_app_name():
    assert settings.app_name == "KRONOS"


def test_app_version():
    assert settings.app_version == "1.0.0"


def test_host():
    assert settings.host == "0.0.0.0"


def test_port():
    assert settings.port == 8000


def test_database_url_exists():
    assert settings.database_url is not None
    assert settings.database_url != ""


def test_secret_key_exists():
    assert settings.secret_key is not None
    assert settings.secret_key != ""


def test_redis_url_exists():
    assert settings.redis_url.startswith("redis://")


def test_celery_broker_exists():
    assert settings.celery_broker_url.startswith("redis://")


def test_celery_backend_exists():
    assert settings.celery_result_backend.startswith("redis://")