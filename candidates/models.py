from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=200)
    vote_number = models.IntegerField()
    votes_quantity = models.IntegerField()