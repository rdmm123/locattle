import json
from secrets import compare_digest

from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from locattle.serializers import LocationSerializer

from .models import CattleLocation


@csrf_exempt
@require_POST
def webhook(request):
    given_token = request.headers.get("X-Downlink-Apikey", "")
    if not compare_digest(given_token, settings.TTN_API_KEY):
        return HttpResponseForbidden(
            "Incorrect token X-Downlink-Apikey header.",
            content_type="text/plain",
        )

    payload = json.loads(request.body)
    print(payload)

    data = payload["uplink_message"]["decoded_payload"]

    CattleLocation.objects.create(
        depto=data["depto"],
        farm=data["finca"],
        cow=data["vaca"],
        lat=data["lat"],
        lng=data["lng"],
        timestamp=payload["received_at"],
    )

    return HttpResponse("ACK", content_type="text/plain")


class CattleLocationView(TemplateView):
    template_name = "locate.html"


class LocationAPIView(GenericAPIView):
    def get(self, request):
        last_location = CattleLocation.objects.order_by("-timestamp").first()
        data = LocationSerializer(last_location).data 
        return Response(data)


class AboutUsView(TemplateView):
    template_name = "about_us.html"