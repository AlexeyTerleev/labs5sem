from django.shortcuts import render
from .models import Exhibits, ExhibitionHalls, Exhibitions
from .forms import ExebitionForm, CityForm
from datetime import date

# Create your views here.


def index(request):
    
    filter_id = request.POST.get("exebition") if request.method == "POST" else 1
    exebition_form = ExebitionForm(initial={"exebition": filter_id})

    exhibits = Exhibits.objects.filter(exhibition_id=filter_id).select_related("artist_id")
    data = []
    for exhibit in exhibits:
        artist_birth_date = exhibit.artist_id.birth_date
        today = date.today()
        data.append(
            {
                "exhibit_name": exhibit.name,
                "artist_name": exhibit.artist_id.name,
                "artist_age": today.year - artist_birth_date.year - ((today.month, today.day) < (artist_birth_date.month, artist_birth_date.day)),
                "exhibit_creation_date": exhibit.date
            }
        )
    return render(request, "index.html", context={"form": exebition_form, "data": data})
    
    
def exhibition_halls(request):
    city_name = request.POST.get("city") if request.method == "POST" else "Минск"
    city_form = CityForm(initial={"city": city_name})

    exhibition_halls = ExhibitionHalls.objects.select_related().filter(adress__icontains=city_name)
    data = []
    for exhibition_hall in exhibition_halls:
        data.append(
            {
                "date": None,
                "name": exhibition_hall.name,
                "address": exhibition_hall.adress,
                "space": exhibition_hall.space,
                "owner": exhibition_hall.owner_id.name,
            }
        )

    return render(request, "test.html", context={"form": city_form, "data": data})


def exhibitions(request):
    city_name = request.POST.get("city") if request.method == "POST" else "Минск"
    city_form = CityForm(initial={"city": city_name})

    exhibitions = Exhibitions.objects.select_related().filter(exhibition_hall_id_id__adress__icontains=city_name)
    data = []
    for exhibition in exhibitions:
        data.append(
            {
                "date": exhibition.date,
                "name": exhibition.name,
                "hall_address": exhibition.exhibition_hall_id.adress,
            }
        )

    return render(request, "exhibitions.html", context={"form": city_form, "data": data})