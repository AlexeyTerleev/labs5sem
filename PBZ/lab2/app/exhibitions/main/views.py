from django.shortcuts import render
from .forms import ExebitionForm

# Create your views here.


def index(request):
    exebition_form = ExebitionForm()
    return render(request, "index.html", {"form": exebition_form})