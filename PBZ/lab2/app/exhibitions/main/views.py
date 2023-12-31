from typing import Any
from django.shortcuts import render
from django.http import HttpRequest
from main.models import Exhibit, ExhibitionHall, Exhibition
from main.forms import ExebitionForm, CityForm,ExhibitForm
from datetime import date



def get_filter(request: HttpRequest, filter_name: str, default_value):
    return request.POST.get(filter_name) if request.method == "POST" else default_value


def get_data_exhibit(exhibit):
    artist_birth_date = exhibit.artist.birth_date
    return {
        "exhibit_name": exhibit.name,
        "artist_name": exhibit.artist.name,
        "artist_birth_year": artist_birth_date.year,
        "exhibit_creation_date": exhibit.date
    }


def get_data_exhibition_hall(exhibition_hall):
    return {
        "date": exhibition_hall.date,
        "name": exhibition_hall.name,
        "address": exhibition_hall.adress,
        "space": exhibition_hall.space,
        "owner": exhibition_hall.owner.name,
    }


def get_data_exhibition(exhibition):
    return {
        "start_date": exhibition.start_date,
        "end_date": exhibition.end_date,
        "name": exhibition.name,
        "hall_address": exhibition.exhibition_hall.adress,
    }


def exhibits(request):
    filter_name, default_value = "exebition", 1
    filter = get_filter(request, filter_name, default_value)
    form = ExebitionForm(initial={filter_name: filter})
    rows = Exhibit.objects.prefetch_related().filter(exhibitions__id=filter).select_related("artist")
    data = [get_data_exhibit(row) for row in rows]
    return render(request, "exhibits.html", context={"form": form, "data": data})
    
    
def exhibition_halls(request):
    filter_name, default_value = "city", "Minsk"
    filter = get_filter(request, filter_name, default_value)
    form = CityForm(initial={filter_name: filter})
    rows = ExhibitionHall.objects.select_related().filter(adress__icontains=filter)
    data = [get_data_exhibition_hall(row) for row in rows]
   
    return render(request, "exhibition_halls.html", context={"form": form, "data": data})


def exhibitions(request):
    filter_name, default_value = "city", "Minsk"
    filter = get_filter(request, filter_name, default_value)
    form = CityForm(initial={filter_name: filter})
    today = date.today()
    rows = Exhibition.objects.select_related().filter(exhibition_hall_id__adress__icontains=filter,start_date__lte=today, end_date__gte=today)
    data = [get_data_exhibition(row) for row in rows]
    return render(request, "exhibitions.html", context={"form": form, "data": data})

def exhibition_by_exhibit(request):
    filter_name, default_value = "exhibit", 1
    filter = get_filter(request, filter_name, default_value)
    print(filter, filter_name)
    form = ExhibitForm(initial={filter_name: filter})
    rows = Exhibition.objects.prefetch_related().filter(exhibit__id=filter).select_related("exhibition_hall")
    print(rows.query.__str__())
    print("test")
    data = [get_data_exhibition(row) for row in rows]
    return render(request, "exhibition_by_exhibit.html", context={"form": form, "data": data})
    