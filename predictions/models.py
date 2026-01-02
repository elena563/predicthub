from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    reputation_score = models.IntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)  
    is_expert = models.BooleanField(default=False)
    saved_predictions = models.ManyToManyField('PredictionEvent', blank=True, related_name='saved_predictions')

    def __str__(self):
        return self.username

class PredictionEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    author = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)

    CATEGORIES = [
        ('sport', 'Sport'),
        ('politics', 'Politics'),
        ('science', 'Science'),
        ('economy', 'Economy'),
        ('weather', 'Weather'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORIES)

    @property
    def status(self):
        now = timezone.now()
        if now < self.start_date:
            return "Not yet started"
        elif self.start_date <= now <= self.end_date:
            return "Active"
        else:
            return "Closed"

    def __str__(self):
        return self.title

class Prediction(models.Model):
    event = models.ForeignKey(PredictionEvent, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    predicted_value = models.FloatField(null=True, blank=True) #add predictiontype, choice prediction
    timestamp = models.DateTimeField(auto_now_add=True)

class Outcome(models.Model):
    event = models.OneToOneField(PredictionEvent, on_delete=models.CASCADE)
    actual_value = models.FloatField(null=True, blank=True) # non è detto che sia numero
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    event = models.ForeignKey(PredictionEvent, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()