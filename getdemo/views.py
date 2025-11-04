from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Coil

# 1) Basic GET API with static response
def static_api(request):
    data = {
        "message": "Welcome to Coil Management API!",
        "status": "success",
        "data": {
            "coil_name": "Test Coil",
            "yard_name": "Yard-A",
            "weight": "10 tons",
            "status": "Available"
        }
    }
    return JsonResponse(data, status=200)


# 2) GET API with dynamic response via query params
def dynamic_api(request):
    coil_name = request.GET.get("coil_name", "Default Coil")
    yard_name = request.GET.get("yard_name", "Default Yard")
    weight = request.GET.get("weight", "0")

    data = {
        "message": "Dynamic Coil Response",
        "status": "success",
        "data": {
            "coil_name": coil_name,
            "yard_name": yard_name,
            "weight": f"{weight} tons"
        }
    }
    return JsonResponse(data, status=200)


# 3) GET API with dynamic request body
@csrf_exempt
def dynamic_body_api(request):
    if request.method == "GET":
        import json
        try:
            body = json.loads(request.body.decode("utf-8"))
            coil_name = body.get("coil_name", "Unknown Coil")
            yard_name = body.get("yard_name", "Unknown Yard")
            weight = body.get("weight", 0)
        except Exception:
            return JsonResponse({"error": "Invalid body"}, status=400)

        data = {
            "message": "Dynamic Body Response",
            "status": "success",
            "data": {
                "coil_name": coil_name,
                "yard_name": yard_name,
                "weight": f"{weight} tons"
            }
        }
        return JsonResponse(data, status=200)

    return JsonResponse({"error": "Only GET allowed"}, status=405)


# 4a) GET API with DB integration → list all coils
def coil_list(request):
    coils = Coil.objects.select_related("yard").values(
        "id",
        "coil_name",
        "weight",
        "status",
        "yard__name"
    )
    return JsonResponse(list(coils), safe=False, status=200)


# 4b) GET API with DB integration → single coil details
def coil_detail(request, pk):
    coil = get_object_or_404(Coil, pk=pk)
    data = {
        "id": coil.id,
        "coil_name": coil.coil_name,
        "yard_name": coil.yard.name,
        "weight": coil.weight,
        "status": coil.status,
    }
    return JsonResponse(data, status=200)


# 5) GET API → merged coil + yard data
def merged_coil_api(request):
    coils = Coil.objects.select_related("yard").values(
        "coil_name",
        "weight",
        "status",
        "yard__name",
        "yard__location"
    )
    return JsonResponse(list(coils), safe=False)




