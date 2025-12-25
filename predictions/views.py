from django.shortcuts import render, redirect
from .models import PredictionEvent
from django.contrib.auth.decorators import login_required
from forms import PredictionForm

def index(request):
    return render(request, "predictions/index.html")

@login_required
def create_prediction_event(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction_event = form.save(commit=False)
            prediction_event.author = request.user.userprofile
            
            prediction_event.save()
            return redirect('prediction_event', pk=prediction_event.pk)
        else:
            return render(request, "create_prediction.html", {
                    'form': PredictionForm(),
                    "error": "Invalid data"
                })
    return render(request, "create_prediction.html", {
        "form": PredictionForm()
    })