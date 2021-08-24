from django.db import models

# Create your models here.

class Boilerplate(models.Model):
    name = models.CharField(max_length=50, null=True)
    file = models.FileField(upload_to="images/", null=True)

    def __str__(self) -> str:
        return self.name