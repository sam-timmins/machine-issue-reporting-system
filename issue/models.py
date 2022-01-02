from django.db import models
from django.contrib.auth.models import AbstractUser


# Status of the machine in Machine
STATUS = ((0, 'Faulty'), (1, 'Working'))


class Machine(models.Model):
    """
    Recording machine information
    """

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"



class User(AbstractUser):
    """
    Customizable User model, inheriting from Django's AbstractUser
    """
    pass
