from django import forms
from .models import Exhibition


class ExebitionForm(forms.Form):
    exebition = forms.ChoiceField(
        choices = tuple((exhibition.id, exhibition.name) for exhibition in Exhibition.objects.all())
    )


class CityForm(forms.Form):
    city = forms.CharField(required=False)

    