from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class UserModel(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = 'user'

    name = models.CharField(max_length=20, validators=[RegexValidator('^[a-zA-Z]{2,20}$', 'name mush be only a-z A-Z, min 2 and max 20 chars')])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    email = models.EmailField()
    gender = models.CharField(max_length=20, default="male", blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
