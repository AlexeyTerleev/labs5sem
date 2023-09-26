from django import forms
from .models import Exhibitions


class ExebitionForm(forms.Form):
    exebition = forms.ChoiceField(
        choices = tuple((exhibition.id, exhibition.name) for exhibition in Exhibitions.objects.all())
    )