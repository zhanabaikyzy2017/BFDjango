from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, UserManager, PermissionsMixin

from django.db.models.signals import post_save
from django.dispatch import receiver


class MyAbstractUser(AbstractUser):
    pass


class MyUser(MyAbstractUser):
    pass
    #
    # def _try_to_create_profile(self,created):
    #     if created:
    #         UserProfile.objects.get_or_create(user=self)
    #
    # def save(self, *args, **kwargs):
    #     print('before saving')
    #
    #     created = self.id is None
    #
    #     super(MyUser,self).save(*args,**kwargs)
    #
    #     self._try_to_create_profile(created)
    #
    #     print('after saving')
    #
    #



class UserProfile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)



