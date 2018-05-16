
from django.db import models

# Create your models here.
class businessCard(models.Model):

    email = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email