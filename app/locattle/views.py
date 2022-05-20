import json
from secrets import compare_digest

from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

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
    )

    return HttpResponse("ACK", content_type="text/plain")