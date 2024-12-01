from django.shortcuts import render
from .models import MainContent

def index(request):
    return render(request, 'product/index.html')

# Create your views here.
