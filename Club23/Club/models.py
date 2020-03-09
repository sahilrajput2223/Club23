from django.db import models

# Create your models here.

occasion = (
    ('Birthday', 'Birthday'),
    ('Wedding', 'Wedding'),
    ('Marriage','Marriage'),
    ('Farewell','Farewell'),
    ('Marriage reception','Marriage reception'),
    ('Festival party','Festival party'),
    ('Other', 'Other'),
)

venu = (
    ('Gym | 2500','Gym'),
    ('Cardio Theater | 3000','Cardio Theater'),
    ('Personal Training Counter | 4000','Personal Training Counter'),
    ('Cycling Studio | 4000','Cycling Studio'),
    ('Luxurious Changing Room | 6000','Luxurious Changing Room'),
    ('Members Lounge | 5000','Members Lounge'),
    ('restaurants | 7000','restaurants'),
    ('swimming pool | 3000','swimming pool'),
)

class Bookclub(models.Model):
    email = models.EmailField()
    Occasion = models.CharField(max_length=25, choices=occasion)
    Time_from = models.TimeField()
    Time_to = models.TimeField()
    Date_from = models.DateField()
    Date_to = models.DateField()
    Venu = models.CharField(max_length=100, choices=venu)

    def __str__(self):
        return self.email

