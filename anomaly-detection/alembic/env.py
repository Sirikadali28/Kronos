import os
from logging.config import fileConfig

from sqlalchemy import create_engine

from alembic import context
from app.db.base import Base

# Import all models
from app.db.detection_history import DetectionHistory  # noqa: F401
from app.db.job_history import JobHistory  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

database_url = os.getenv("DATABASE_URL")

if database_url:
    database_url = database_url.replace(
        "postgresql+asyncpg",
        "postgresql+psycopg",
    )


def run_migrations_offline():
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    engine = create_engine(database_url)

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
