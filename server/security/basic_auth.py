import base64

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from backend.models import User


class BasicAuth(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header:
            return None

        auth_header = auth_header.split()
        if len(auth_header) != 2 or auth_header[0].lower() != 'basic':
            return None

        try:
            auth_decoded = base64.b64decode(auth_header[1]).decode('utf-8')
            username, password = auth_decoded.split(':')
        except (ValueError, TypeError):
            raise AuthenticationFailed('Invalid basic header. Credentials not provided.')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('User does not exist.')

        if user.password != password:
            raise AuthenticationFailed('Invalid password.')
        user.is_authenticated = True
        return (user, None)
