from django.db import models


class Ability(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='abilitys/images')

    def __str__(self):
        return self.title


