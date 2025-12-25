from django import forms
from .models import PredictionEvent

class PredictionForm(forms.ModelForm):
    class Meta:
        model = PredictionEvent
        fields = ['title', 'description', 'start_date', 'end_date', 'category']