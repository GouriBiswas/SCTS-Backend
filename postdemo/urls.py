from django.urls import path
from . import views

urlpatterns = [
    path('static-post/', views.static_post),      # Task 1
    path("dynamic-coil/", views.dynamic_coil_post, name="dynamic_coil_post"),
    path('body-post/', views.body_post),          # Task 3
    path('db-post/', views.db_post),              # Task 4
    path('db-get/', views.db_get),                # Extra GET API to fetch coils
]
