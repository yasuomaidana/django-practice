from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from backend.models import User
from serializer.user_serializer import UserSerializer


@api_view(['GET'])
def get_user(request: Request):
    user_id = request.GET.get('username')
    if user_id:
        user = User.objects.get(username=user_id)
    else:
        user = User.objects.first()
    serializer = UserSerializer(user)
    return Response(serializer.data)
