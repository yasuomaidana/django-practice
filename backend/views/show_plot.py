from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import api_view


@api_view(['GET'])
def show_plot(request):
    return render(request, 'show_plot.html')
