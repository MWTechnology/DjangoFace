from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name="Адрес электронной почты", max_length=200)
    number = models.CharField("Номер удостоверения", max_length=100)
    is_active = models.BooleanField(('Активный пользователь'), default=False)


    def __str__(self):
        return '%s %s' % (self.username, self.email)



    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'