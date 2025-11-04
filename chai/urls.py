
from django.urls import path
from . import views
from .views import chai_static_api
from .views import coils_api


# localhost:8000/chai
# localhost:8000/chai/order
urlpatterns = [
     path('', views.all_chai, name='all_chai'),
       path("chai-api/", views.chai_static_api, name="chai_static_api"),
      path("coils-api/", views.coils_api, name='coils_api')
]