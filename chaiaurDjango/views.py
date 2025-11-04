from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   #  return HttpResponse("Hello, world. You are at Hitachi Home Page")
   # dynamic data    
   peoples = [
       {'name' : 'Gouri Biswas', 'age' : 22},
       {'name' : 'Soma Biswas', 'age' : 48},
       {'name' : 'Pratyush Biswas', 'age' : 55},
       {'name' : 'Gourav Biswas', 'age' : 15},
       {'name' : 'Shegaonkar', 'age' : 23},

   ]
   for people in peoples:
       print(people)
       
       text = """
       Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam quas eveniet sequi ad, quidem a iste ducimus eligendi quasi natus voluptates iusto, rerum laudantium nulla quia facilis. Laudantium temporibus illum nostrum."""


   return render(request, 'website/index.html' , context = {'peoples' : peoples, 'text' : text})

def about(request):
    # return HttpResponse("Hello, world. You are at Hitachi About Page")
    return render(request , 'website/about.html')

def contact(request):
    # return HttpResponse("Hello, world. You are at Hitachi Contact Page")
    return render(request , 'website/contact.html')