from django import forms
from .models import PredictionEvent, UserProfile

class PredictionForm(forms.ModelForm):
    class Meta:
        model = PredictionEvent
        fields = ['title', 'description', 'start_date', 'end_date', 'category']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'bio', 'is_expert', 'is_admin']