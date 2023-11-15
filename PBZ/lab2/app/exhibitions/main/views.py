from typing import Any
from django.shortcuts import render
from django.http import HttpRequest
from .models import Exhibits, ExhibitionHalls, Exhibitions
from .forms import ExebitionForm, CityForm
from datetime import date



def get_filter(request: HttpRequest, filter_name: str, default_value):
    return request.POST.get(filter_name) if request.method == "POST" else default_value


def get_data_exhibit(exhibit):
    artist_birth_date = exhibit.artist_id.birth_date
    today = date.today()
    age = today.year - artist_birth_date.year - ((today.month, today.day) < (artist_birth_date.month, artist_birth_date.day))
    return {
        "exhibit_name": exhibit.name,
        "artist_name": exhibit.artist_id.name,
        "artist_age": age,
        "exhibit_creation_date": exhibit.date
    }


def get_data_exhibition_hall(exhibition_hall):
    return {
        "date": exhibition_hall.date,
        "name": exhibition_hall.name,
        "address": exhibition_hall.adress,
        "space": exhibition_hall.space,
        "owner": exhibition_hall.owner_id.name,
    }


def get_data_exhibition(exhibition):
    return {
        "date": exhibition.date,
        "name": exhibition.name,
        "hall_address": exhibition.exhibition_hall_id.adress,
    }


def exhibits(request):
    filter_name, default_value = "exebition", 1
    filter = get_filter(request, filter_name, default_value)
    form = ExebitionForm(initial={filter_name: filter})

    rows = Exhibits.objects.prefetch_related().filter(exhibitions__id=filter).select_related("artist_id")
    print(rows.query.__str__())
    print("test")
    data = [get_data_exhibit(row) for row in rows]
    return render(request, "exhibits.html", context={"form": form, "data": data})
    
    
def exhibition_halls(request):
    filter_name, default_value = "city", "Minsk"
    filter = get_filter(request, filter_name, default_value)
    form = CityForm(initial={filter_name: filter})
    rows = ExhibitionHalls.objects.select_related().filter(adress__icontains=filter)
    data = [get_data_exhibition_hall(row) for row in rows]
   
    return render(request, "exhibition_halls.html", context={"form": form, "data": data})


def exhibitions(request):
    filter_name, default_value = "city", "Minsk"
    filter = get_filter(request, filter_name, default_value)
    form = CityForm(initial={filter_name: filter})
    rows = Exhibitions.objects.select_related().filter(exhibition_hall_id_id__adress__icontains=filter)
    data = [get_data_exhibition(row) for row in rows]
    return render(request, "exhibitions.html", context={"form": form, "data": data})