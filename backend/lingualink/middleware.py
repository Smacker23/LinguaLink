from django.http import JsonResponse
from django.conf import settings

class BlockUnauthorizedOriginsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_origins = set(settings.CORS_ALLOWED_ORIGINS)

        # Get the Origin header from the request
        origin = request.headers.get("Origin")

        # If an origin is present and not in the allowed list, reject the request
        if origin and origin not in allowed_origins:
            return JsonResponse({"error": "Unauthorized origin"}, status=403)

        return self.get_response(request)
