from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    # Link booking to a specific user to enable history tracking
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    event_date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event_date}"
