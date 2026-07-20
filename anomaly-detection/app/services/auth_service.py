from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.db.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import Token, UserCreate


class AuthService:
    """
    Service responsible for authentication.
    """

    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository

    async def register(
        self,
        user_data: UserCreate,
    ) -> User:
        """
        Register a new user.
        """

        existing_user = await self.repository.get_by_email(
            user_data.email,
        )

        if existing_user:
            raise ValueError("User already exists.")

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hash_password(
                user_data.password,
            ),
        )

        return await self.repository.create(user)

    async def login(
        self,
        email: str,
        password: str,
    ) -> Token:
        """
        Authenticate a user.
        """

        user = await self.repository.get_by_email(
            email,
        )

        if user is None:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password.")

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role,
                "user_id": user.id,
            }
        )

        return Token(
            access_token=token,
        )
