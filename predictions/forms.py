from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PredictionEvent, UserProfile

class PredictionForm(forms.ModelForm):
    class Meta:
        model = PredictionEvent
        fields = ['title', 'description', 'start_date', 'end_date', 'category']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100, required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    is_expert = forms.BooleanField(required=False)
    is_admin = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'full_name', 'bio', 'is_expert', 'is_admin']