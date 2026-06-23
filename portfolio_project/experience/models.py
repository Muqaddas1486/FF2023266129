from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    duration = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.title