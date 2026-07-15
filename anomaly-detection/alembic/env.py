from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config, pool

from alembic import context

from app.db.base import Base

# Import all models so Alembic can detect them
from app.db.detection_history import DetectionHistory  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in offline mode."""

    # Use DATABASE_URL from environment, fallback to config
    url = os.getenv("DATABASE_URL") or config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in online mode."""

    # Use DATABASE_URL from environment if available
    database_url = os.getenv("DATABASE_URL")
    
    if database_url:
        # Use asyncpg URL as-is for async migrations
        configuration = {
            "sqlalchemy.url": database_url,
            "sqlalchemy.poolclass": pool.NullPool,
        }
    else:
        configuration = config.get_section(config.config_ini_section)

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
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