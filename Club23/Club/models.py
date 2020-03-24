from django.db import models

# Create your models here.


class Bookclub(models.Model):
    email = models.EmailField()
    Occasion = models.CharField(max_length=25)
    Price = models.CharField(max_length=10, null=True, blank=True)
    person = models.CharField(max_length=10, null=True, blank=True)
    Time_from = models.TimeField()
    Time_to = models.TimeField()
    Date_from = models.DateField()
    Date_to = models.DateField()
    Venu = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Payment(models.Model):
    u_name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.u_name


class News(models.Model):
    Occasion = models.CharField(max_length=10)
    Bio = models.TextField()
    Date = models.DateField()
    Time = models.TimeField()

    def __str__(self):
        return self.Occasion

