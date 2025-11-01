# app/db/engine.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool
from app.core.config import settings

def _asyncpg_url(url: str) -> str:
    # Convert postgres[ql]://... to postgresql+asyncpg://...
    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql+asyncpg://", 1)
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+asyncpg://", 1)
    return url  # already correct

DATABASE_URL = _asyncpg_url(settings.SUPABASE_DB_URL)

engine = create_async_engine(
    DATABASE_URL,
    poolclass=NullPool,                 # PgBouncer is your pool
    pool_pre_ping=False,               # not needed with PgBouncer
    connect_args={
        # PgBouncer (transaction mode) + asyncpg:
        # disable prepared statements to avoid “does not support PREPARE”
        "statement_cache_size": 0,             # asyncpg <= 0.29 name
        "prepared_statement_cache_size": 0,    # asyncpg >= 0.29 name (harmless if unknown)
        # optional: enforce TLS if your URI lacks it
        # "ssl": True,  # or include ?sslmode=require in the URL
    },
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

