from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


# Status of the machine in Machine
STATUS = ((0, 'Faulty'), (1, 'Working'))
# Status of the issue in Issue
ISSUE_RECTIFIED = ((0, 'Not Rectified'), (1, 'Rectified'))
# Text displayed if user is deleted
DELETED_USER = 'Deleted User'


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


class Issue(models.Model):
    """
    Recording issue information
    """
    
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='issues')
    user = models.ForeignKey(User, on_delete=models.SET(DELETED_USER), null=True, related_name="issue_username")
    rectified = models.IntegerField(choices=ISSUE_RECTIFIED, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.machine}"


class User(AbstractUser):
    """
    Customizable User model, inheriting from Django's AbstractUser
    """
    pass
