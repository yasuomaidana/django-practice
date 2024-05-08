from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def general_view(request):
    try:
        first_user = User.objects.first()
        return HttpResponse(f"Hi {first_user.username}!")
    except AttributeError:
        return HttpResponse("Empty")
