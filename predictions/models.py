from django.db import models

# Create your models here.
class PredictionEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50)

class Prediction(models.Model):
    event = models.ForeignKey(PredictionEvent, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    predicted_value = models.FloatField() # non è detto che sia numero
    timestamp = models.DateTimeField(auto_now_add=True)

class Outcome(models.Model):
    event = models.OneToOneField(PredictionEvent, on_delete=models.CASCADE)
    actual_value = models.FloatField() # non è detto che sia numero
    timestamp = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    reputation_score = models.IntegerField(default=0)
    bio = models.TextField(blank=True, null=True)

