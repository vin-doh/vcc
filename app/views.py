from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    context = {}

    return render(request, "index.html", context)