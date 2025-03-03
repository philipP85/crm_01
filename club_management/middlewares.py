from django.shortcuts import redirect
from django.conf import settings

class LoginRequiredMiddleware:
    """ Middleware, um alle Seiten nur für eingeloggte Nutzer freizugeben. """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Wenn der User nicht eingeloggt ist und NICHT auf einer Login- oder Logout-Seite
        if not request.user.is_authenticated and request.path not in [settings.LOGIN_URL, settings.LOGOUT_REDIRECT_URL]:
            return redirect(settings.LOGIN_URL)  # Zum Login umleiten
        return self.get_response(request)
