from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    user_type = models.IntegerField(default=0, null=True, blank=True)
    user_status = models.IntegerField(default=0, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', u'male'), ('female', u'female')), default='male')
    address = models.CharField(max_length=100, default=u'', null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png')

    class Meta:
        db_table = "auth_users"

    def __unicode__(self):
        return self.username
