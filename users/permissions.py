from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from users.models import User

class IsAuthenticatedWithToken(BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.from_request(request, anonymous_raise_401=True)
            if user is None:
                return False
            request.user = user 
            return True
        except AuthenticationFailed as e:
            raise AuthenticationFailed(
                detail={"message": "Authentication failed", "code": "authentication_failed"}
            )