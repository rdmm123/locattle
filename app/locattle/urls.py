from django.urls import path
from locattle.views import AboutUsView, CattleLocationView, LocationAPIView

from locattle.views import webhook

urlpatterns = [
    path('webhook/', webhook, name='webhook'),
    path('', CattleLocationView.as_view(), name="locattle"),
    path('about/', AboutUsView.as_view(), name="about_us"),
    path('api/last_location/', LocationAPIView.as_view(), name="location-api")
]