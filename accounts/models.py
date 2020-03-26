from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    user_type_choices = (
        ('admin', 'admin'),
        ('staff', 'staff'),
        ('customer', 'customer')
    )

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=user_type_choices)
    # user_role
    is_super_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
