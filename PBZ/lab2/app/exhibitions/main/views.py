from django.shortcuts import render
from .models import Exhibits
from .forms import ExebitionForm
from datetime import date

# Create your views here.


def index(request):
    
    filter_id = request.POST.get("exebition") if request.method == "POST" else 1
    exebition_form = ExebitionForm(initial={"exebition": filter_id})
    
    exhibits = Exhibits.objects.filter(exhibition_id=filter_id).select_related("artist_id")
    print(filter_id)
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
    
    