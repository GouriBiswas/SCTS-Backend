# from django.urls import path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/coils/$', consumers.CoilConsumer.as_asgi()),
# ]


from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/coils/$', consumers.CoilConsumer.as_asgi()),
]
