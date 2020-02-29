from django.db import models

# Create your models here.

occasion = (
    ('Birthday', 'Birthday'),
    ('Wedding', 'Wedding'),
    ('Marriage','Marriage'),
    ('Farewell','Farewell'),
    ('Marriage reception','Marriage reception'),
    ('Festival party','Festival party'),
)
class Bookclub(models.Model):
    email = models.EmailField()
    Occasion = models.CharField(max_length=25, choices=occasion)
    Time_from = models.TimeField()
    Time_to = models.TimeField()
    Date_from = models.DateField()
    Date_to = models.DateField()

    def __str__(self):
        return self.email
