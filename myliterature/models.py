from django.db import models

class Literature(models.Model):
    name        =models.CharField(max_length=23)
    title       =models.CharField(max_length=32)
    description =models.TextField(blank=True, null=True)
    literature  =models.FileField()

    def __str__(self):
        return self.title
# Create your models here.