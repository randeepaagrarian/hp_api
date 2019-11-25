import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . models import Contract

def index(request):
    return JsonResponse({"status": "true", "data": "/contract"}, safe=False)

@csrf_exempt
def schedule(request, capital, installments, installment_interval, rate, initiation_date, method):
    contract = Contract(capital, installments, installment_interval, rate, initiation_date, method)
    response = {
        "status": "true",
        "data": {
            "schedule": contract.get_schedule()
        }
    }
    return JsonResponse(response, safe=False)