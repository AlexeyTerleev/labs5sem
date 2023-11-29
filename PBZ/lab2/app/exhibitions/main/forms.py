from django import forms
from .models import Exhibition, Exhibit


class ExebitionForm(forms.Form):
    exebition = forms.ChoiceField(
        choices = tuple((exhibition.id, exhibition.name) for exhibition in Exhibition.objects.all())
    )


class ExhibitForm(forms.Form):
    exhibit = forms.ChoiceField(
        choices = tuple((exhibit.id, exhibit.name) for exhibit in Exhibit.objects.all())
    )


class CityForm(forms.Form):
    city = forms.CharField(required=False)

    