from django.db import models
from django.contrib.auth.models import AbstractUser


# Status of the machine in Machine
STATUS = ((0, 'Faulty'), (1, 'Working'))


class User(AbstractUser):
    pass
