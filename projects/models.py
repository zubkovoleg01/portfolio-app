from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date_completed = models.DateField()
    image = models.ImageField(upload_to='projects/images')
    download_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title