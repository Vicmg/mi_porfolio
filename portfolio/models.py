from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    date = models.DateTimeField(null=True,blank=True)
    url = URLField(blank=True)

#user: victor
#pass: operacion95