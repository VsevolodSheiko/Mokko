from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import *
from coffeehouse.serializers import RegistrationSerializer

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response(data={"status": "ok"})
    else:
        return Response(data={"status": "error", "message": "Wrong username or password"}, status=400)


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid() == True:
        user = serializer.save()
        return Response({'status': 'ok', 'user': user.username})
    else:
        return Response({'status': 'error', 'message': serializer.errors}, status=400)


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def logout_view(request):
    logout(request=request)
    return Response({'detail': 'You have been successfully logged out.'}, status=200)