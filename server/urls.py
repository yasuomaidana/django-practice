"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from backend.views.general_view import general_view, general_view2
from backend.views.plot_view import plot_function, PlotFunctionView
from backend.views.show_plot import show_plot

urlpatterns = [
    path("admin/", admin.site.urls),
    path("general/", general_view, name="general_view"),
    path("general2/", general_view2),
    path("plot/", plot_function, name="plot_function"),
    path("plot2/", PlotFunctionView.as_view(), name="plot_function2"),
    path("show_plot/", show_plot, name="show_plot"),
]
