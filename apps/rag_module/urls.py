from django.urls import path
from .views import hello_rag

urlpatterns = [
    path("hello/", hello_rag),
]
