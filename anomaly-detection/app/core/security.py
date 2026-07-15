from datetime import datetime, timedelta, UTC

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

# JWT configuration
ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    """
    Hash a plain-text password.
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verify a plain-text password against its hash.
    """
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
) -> str:
    """
    Create a JWT access token.
    """
    to_encode = data.copy()

    expire = (
        datetime.now(UTC)
        + (
            expires_delta
            if expires_delta
            else timedelta(minutes=60)
        )
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=ALGORITHM,
    )


def verify_access_token(
    token: str,
):
    """
    Decode and verify a JWT token.
    """
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[ALGORITHM],
        )
        return payload

    except JWTError:
        return None