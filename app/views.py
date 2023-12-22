from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    context = {"year": datetime.now().year}
    return render(request, "index.html", context)
