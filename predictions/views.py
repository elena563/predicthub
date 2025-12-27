from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.models import User

from .forms import PredictionForm, RegistrationForm
from .models import PredictionEvent, UserProfile, Comment

def index(request):
    predictions = PredictionEvent.objects.all()
    return render(request, "predictions/index.html", predictions=predictions)

def login(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "predictions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "predictions/login.html")

def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            bio = form.cleaned_data.get("bio", "")
            is_expert = form.cleaned_data.get("is_expert", False)
            is_admin = form.cleaned_data.get("is_admin", False)

            user = User.objects.create_user(username=username, email=email, password=password)

            UserProfile.objects.create(
                user=user,
                username=username,
                email=email,
                bio=bio,
                is_expert=is_expert,
                is_admin=is_admin
            )
            login(request, user)
            return redirect("index")
        else:
            return render(request, "predictions/register.html", {
                    'form': RegistrationForm(),
                    "error": "Invalid data"
                })
    else:
        form = RegistrationForm()
        return render(request, "predictions/register.html", {"form": form})
    

@login_required
def create_prediction_event(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction_event = form.save(commit=False)
            prediction_event.author = request.user.userprofile
            
            prediction_event.save()
            return redirect('prediction', pk=prediction_event.pk)
        else:
            return render(request, "predictions/create_prediction.html", {
                    'form': PredictionForm(),
                    "error": "Invalid data"
                })
    return render(request, "predictions/create_prediction.html", {
        "form": PredictionForm()
    })

def predictionPage(request, id): 
    predEvent = PredictionEvent.objects.filter(id=id).first()

    if predEvent is not None:
        return render(request, "predictions/prediction.html", {
            "prediction": predEvent
        })
    else:
        return render(request, "predictions/index.html", {
            "error": "Prediction event has been deleted or removed"
        })
    
@login_required
def comment(request, id):
    if request.method == 'POST':
        predEvent = PredictionEvent.objects.get(id=id)
        comment_text = request.POST.get("comment")
        Comment.objects.create(
            predEvent=predEvent,
            author=request.user,
            text=comment_text
        )
        return redirect('prediction', pk=predEvent.pk)
    
def saved(request):
    return render(request, "predictions/saved.html", {
            "user": request.user,
        })

def save(request, name):
    predEvent = PredictionEvent.objects.get(name=name)
    if request.user.saved_predictions.filter(pk=predEvent.pk).exists():
        request.user.saved_predictions.remove(predEvent)
        return render(request, "predictions/prediction.html", {
                    "predEvent": predEvent,
                "message": "Removed!"
        })
    else:
        request.user.saved_predictions.add(predEvent)
        return render(request, "predictions/prediction.html", {
            "predEvent": predEvent,
            "message": "Added!"
        })
    
def delete(request, id):
    if request.method == "POST":
        predEvent = PredictionEvent.objects.get(id=id)
        predEvent.delete()
    return redirect('')
