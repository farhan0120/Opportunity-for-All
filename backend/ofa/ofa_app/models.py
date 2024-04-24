from django.db import models

# Create your models here.

class Opportunity(models.Model):
    category = models.CharField(max_length=100)
    program_name = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    things_needed = models.TextField(blank=True)  # Allow the field to be blank
    deadline = models.DateField(null=True, blank=True)  # Allow the field to be null and blank

    def __str__(self):
        return self.program_name