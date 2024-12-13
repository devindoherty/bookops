"""
URL configuration for bookops project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

from . import views

urlpatterns = [
    path("manuscripts/", views.manuscripts, name="manuscripts"),
    path("manuscripts/<str:get>", views.get_manuscripts, name="get_manuscripts"),
    path("manuscript/<int:id>", views.get_manuscript, name="get_manuscript"),
    path("manuscript/edit/<int:id>", views.edit_manuscript, name="edit_manuscript")
]

