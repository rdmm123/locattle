from django.urls import path
from locattle.views import CattleLocationView

from locattle.views import webhook

urlpatterns = [
    path('webhook/', webhook, name='webhook'),
    path('', CattleLocationView.as_view(), name="locattle")
]