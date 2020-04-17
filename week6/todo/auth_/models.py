from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, UserManager, PermissionsMixin


class MyAbstractUser(AbstractUser):
    pass


class MyUser(MyAbstractUser):
    pass

