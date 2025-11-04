from django.urls import path
from . import views

urlpatterns = [
    path("static/", views.static_api, name="static_api"),
    path("dynamic/", views.dynamic_api, name="dynamic_api"),
    path("dynamic-body/", views.dynamic_body_api, name="dynamic_body_api"),
    path("coils/", views.coil_list, name="coil_list"),
    path("coils/<int:pk>/", views.coil_detail, name="coil_detail"),
        path("merged-coils/", views.merged_coil_api, name="merged_coil_api"),
    # URL: /coils/<int:pk>/ → <int:pk> means a placeholder for a number (primary key).
    # Fetches one coil with the given id (pk).
]

# path → Django function used to map a URL to a view.
# Each path() tells Django:
# When a request comes for this URL, call this view function from views.py
# Each path has a name parameter:
# name="static_api" → allows referring to this URL pattern elsewhere in Django (like in templates).


# urls.py is a router for mera application.
# It maps specific API endpoints (like /coils/, /dynamic/) to their respective view functions (views.coil_list, views.dynamic_api, etc.).
# This is what makes your Django API accessible via URLs.