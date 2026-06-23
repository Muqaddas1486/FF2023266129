from django.db import models

# Create your models here.
from django.db import models

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    level = models.IntegerField(default=80)

    def __str__(self):
        return self.skill_name