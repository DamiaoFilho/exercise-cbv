from django import forms
from .models import Reserve, Room, Client

class ReserveForm(forms.ModelForm):

    class Meta:
        model = Reserve
        fields = "__all__"
        widgets = {
            "date_entry": forms.DateInput(attrs={"type":"date", "class":"form-control"}),
            "date_out": forms.DateInput(attrs={"type":"date", "class":"form-control"}),
            "value": forms.NumberInput(attrs={"class":"form-control"}),
            "client": forms.Select(attrs={"class":"form-control"}),
            "room": forms.Select(attrs={"class":"form-control"}),
        }