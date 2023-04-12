from rest_framework import authentication
from django.contrib.auth.models import User

class IPAddressAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request, **kwargs):
        # Get the client's IP address from the request object
        client_ip = request.META.get('REMOTE_ADDR')

        # Check if the client's IP matches the allowed IP address
        if client_ip == '127.0.0.1': #  write here static ip address
            user = User.objects.get(username="root")
        return (user, None)

