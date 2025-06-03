from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self) -> str:
        return f'[{self.id}] {self.first_name} {self.last_name}'

