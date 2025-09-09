from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    mobile = models.TextField()
    people = models.IntegerField()
    check_in = models.DateField()
    ROOM_TYPE_CHOICES = [
    ('single', 'Single'),
    ('double', 'Double'),
    ('suite', 'Suite'),
    ]
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)

    def __str__(self):
        return self.name
    
    