# from django.shortcuts import render
# from .models import ChaiVarity
# from django.http import JsonResponse



# # Create your views here.
# def all_chai(request):
#     chais = ChaiVarity.objects.all()
#     return render(request, 'chai/all_chai.html', {'chais': chais})


from django.shortcuts import render
from django.http import JsonResponse
from .models import ChaiVarity

# Existing HTML view
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

# New GET API (static response)
def chai_static_api(request):
    return JsonResponse({
        "message": "Welcome to the Chai Wala API!",
        "status": "success",
        "data": {
            "chai": "Masala Chai",
            "price": "₹20"
        }
    })


# Coils kai liye get api static reponser
def coils_api(request):
    response_data = {
        "message": "Welcome to the Coils API!",
        "status": "success",
        "data": {
            "coilType": "Copper Coil",
            "yardage": "50 meters",
            "price": "₹500"
        }
    }
    return JsonResponse(response_data)