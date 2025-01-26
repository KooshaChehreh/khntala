import jwt_auth
import time
from typing import Dict, Tuple
from datetime import datetime, timedelta
from django.conf import settings
from users.models import User


def generate_access_token(user: User) -> str:
    time_now = time.time()
    base_payload = {
        "exp": time_now + timedelta(settings.JWT_EXPIRATION_SECS),  # Expiration at (seconds)
        "iat": time_now,  # Issued at (seconds)
        "id": user.id,
        "phone": user.phone,
    }
    return jwt_auth.encode(base_payload, settings.JWT_PRIVATE_KEY, algorithm="RS256")


