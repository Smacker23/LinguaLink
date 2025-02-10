from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

class CookieTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        auth_result = super().authenticate(request)
        if auth_result:
            return auth_result  
        token_key = request.COOKIES.get('auth_token')
        if not token_key:
            return None  
        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token in cookies.')

        return (token.user, token)
