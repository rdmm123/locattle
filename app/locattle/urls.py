from django.urls import path

from locattle.views import webhook

urlpatterns = [
    path('webhook/', webhook, name='webhook'),
]