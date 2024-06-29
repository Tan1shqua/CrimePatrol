from sqlite3 import Date
from django.db import models
from django.contrib.auth.models import User

class CrimeReport(models.Model):
    CRIME_TYPES = [
        ('Theft', 'Theft'),
        ('Vandalism', 'Vandalism'),
        ('Assault', 'Assault'),
        ('Harassment', 'Harassment'),
        ('Murder', 'Murder'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=Date.today)
    time = models.TimeField()
    location = models.CharField(max_length=200)
    crime_type = models.CharField(max_length=50, choices=CRIME_TYPES)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.crime_type} reported by {self.user.username} on {self.date} at {self.time}'
