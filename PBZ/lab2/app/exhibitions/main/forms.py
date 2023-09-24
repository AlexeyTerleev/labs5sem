from django import forms


class ExebitionForm(forms.Form):
    exebition = forms.ChoiceField(
        choices = (
            (1, "test1"), 
            (2, "test2"),
        )
    )