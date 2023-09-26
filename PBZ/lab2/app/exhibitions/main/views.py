from django.shortcuts import render
from .models import Exhibits
from .forms import ExebitionForm

# Create your views here.


def index(request):
    exebition_form = ExebitionForm()
    exhibits = Exhibits.objects.all()
    return render(request, "index.html", {"form": exebition_form, "exhibits": exhibits})