from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    collector = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    cover = models.CharField(max_length=50, blank=True, null=True)
    storyline = models.TextField(max_length=500, blank=True, null=True)
    summary = models.TextField(max_length=500, blank=True, null=True)
    genre_set = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

       
class Collection(models.Model):
    # from .views import save
    # collector = models.ForeignKey(User, on_delete=models.CASCADE)
    # colletion = models.ManyToOneRel(save, null=True, blank=True)
    
    # def __str__(self):
    #     return self.name 
    pass


class Counter(models.Model):
    def increment(self):
        self.counter += 1
    def get_value(self):
        return self.counter
