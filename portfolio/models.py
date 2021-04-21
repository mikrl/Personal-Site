from django.db import models
from django.contrib.auth.models import User

from utilities.models import BaseModel


class Statement(BaseModel):
    title = models.CharField(max_length=40)
    content = models.TextField()
    url_info = models.URLField(blank=True)
    
        
# class ImageLink(BaseModel):
#     image = models.ImageField(upload_to='main')
#     alttext = models.TextField()
        
class Project(BaseModel):
    STATUS = (
        (0, "Planning"),
        (1, "Development"),
        (2, "Maintaining"),
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()    
    status = models.IntegerField(choices=STATUS)
    url = models.URLField()

    class Meta:
        ordering = ['-modified_date']
    
    def __str__(self):
        return self.title


class Certification(models.Model):
    LEVEL = (
        (0, "Beginner"),
        (1, "Intermediate"),
        (2, "Advanced"),
    )
    name = models.CharField(max_length=50, unique=True)
    badge = models.ImageField(blank=True, upload_to='certs')
    expiration_date = models.DateField(blank=True)
    url = models.URLField()
    level = models.IntegerField(choices=LEVEL)

    class Meta:
        ordering = ['-level']
    
    def expires(self):
        """
        Whether the certification expires or not.
        """
        if self.expiration_date:
            return True
        return False
    
    def __str__(self):
        return self.name
