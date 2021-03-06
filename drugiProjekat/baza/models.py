from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    num_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return self.content

    def is_popular(self):
        return self.num_views > 5


# class Review(models.Model):
#     content = models.CharField(max_length=200)
#     num_views = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#
#
# class EnginesPlts(models.Model):
#     content = models.CharField(max_length=200)
#     num_views = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#
#
# class Options(models.Model):
#     content = models.CharField(max_length=200)
#     num_views = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)


    def __str__(self):
        return self.content
