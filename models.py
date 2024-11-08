from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default=USER)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='events_user_groups',  # Unique related name for the reverse relationship
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='events_user_permissions',  # Unique related name for the reverse relationship
        blank=True
    )

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    total_tickets = models.IntegerField()
    tickets_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.event.name} by {self.user.username}"
