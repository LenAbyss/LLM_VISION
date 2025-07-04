from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello_rag(request):
    return JsonResponse({"message": "Hello from RAG module!"})
