from django.urls import path
from locattle.views import CattleLocationView, LocationAPIView

from locattle.views import webhook

urlpatterns = [
    path('webhook/', webhook, name='webhook'),
    path('', CattleLocationView.as_view(), name="locattle"),
    path('api/last_location/', LocationAPIView.as_view(), name="location-api")
]