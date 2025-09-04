from django.conf import settings
import jwt
from datetime import datetime, timedelta, timezone
from jwt import InvalidTokenError, ExpiredSignatureError

from src.supports import AppExceptionCase
class Token:

    @staticmethod
    def create_token(user_id: str):
        expire_time = datetime.now(timezone.utc) + timedelta(days=2)

        payload = {
            "sub": user_id,
            "exp": expire_time
        }

        return jwt.encode(payload, settings.SECRET_TOKEN_KEY, algorithm=settings.SECRET_TOKEN_ALGO)
    
    @staticmethod
    def verify_token(token: str):
        
        try:
            token_data = jwt.decode(token, settings.SECRET_TOKEN_KEY, algorithms=settings.SECRET_TOKEN_ALGO)
            return token_data
        except (InvalidTokenError, ExpiredSignatureError):
            raise AppExceptionCase.UnAuthorized("Invalid or Expire Token")