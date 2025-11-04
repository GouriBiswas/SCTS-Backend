from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Coil

# 1. Static Response
@csrf_exempt
def static_post(request):
    if request.method == "POST":
        return JsonResponse({"message": "This is a static POST API for Coils!"})
    
#2. Dynamic Response with Random Data
import random
@csrf_exempt
def dynamic_coil_post(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            coil_name = body.get("coil_name", "Unnamed Coil")
            weight = body.get("weight", random.uniform(500, 2000))  # use user weight or random
            # request.body → contains the raw request data in bytes.
            # .decode("utf-8") → converts bytes into a readable string.
            # json.loads() → parses the JSON string into a Python dictionary.
            
            # Random statuses for coil
            statuses = ["Available", "Dispatched", "Processing", "On Hold"]
            status = random.choice(statuses)

            # Random coil_id generator
            coil_id = random.randint(1000, 9999)

            return JsonResponse({
                "message": f"Coil '{coil_name}' received successfully!",
                "coil_id": coil_id,
                "coil_name": coil_name,
                "weight": f"{weight} tons",
                "status": status
            })
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
# 3. Dynamic Request Body
@csrf_exempt
def body_post(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        coil_name = data.get("coil_name", "Unknown Coil")
        coil_type = data.get("coil_type", "Generic")
        return JsonResponse({
            "message": f"Coil {coil_name} of type {coil_type} received!"
        })


# 4. DB Integration - Insert coil data
@csrf_exempt
def db_post(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        coil = Coil.objects.create(
            coil_name=data.get("coil_name"),
            coil_type=data.get("coil_type"),
            weight=data.get("weight", 0.0),
            status=data.get("status", "Available")
        )
        return JsonResponse({
            "message": "Coil created successfully",
            "id": coil.id,
            "coil_name": coil.coil_name
        })


# Extra: DB Integration - Fetch coil data
def db_get(request):
    coils = Coil.objects.all().values("coil_name", "coil_type", "weight", "status")
    return JsonResponse({"coils": list(coils)})
     

