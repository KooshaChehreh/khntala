import jwt_auth
import logging

from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from users.models import User



class JWTAuthentication(BaseAuthentication):
    keyword = "JWT"

    def authenticate_header(self, request):
        return 'Bearer realm="api"'

    def authenticate(self, request):
        authenticated_user = User.from_request(
            request=request, anonymous_raise_401=False
        )
        if authenticated_user is None:
            return None
        return (authenticated_user, None)