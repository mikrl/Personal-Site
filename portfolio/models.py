from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Planning"),
    (1, "Development"),
    (2, "Maintaining")
)

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()    
    status = models.IntegerField(choices=STATUS)
    url = models.URLField()
    
    def __str__(self):
        return self.title



