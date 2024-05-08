from django.http import HttpResponse
from django.shortcuts import render

from backend.models import User


def general_view(request):
    try:
        first_user = User.objects.first()
        return HttpResponse(f"Hi {first_user.username}!")
    except AttributeError:
        return HttpResponse("Empty")


def general_view2(request):
    try:
        first_user = User.objects.first()
        return render(request, "general.html", {"username": first_user.username})
    except AttributeError:
        return HttpResponse("Empty")
