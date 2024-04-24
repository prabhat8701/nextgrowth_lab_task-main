from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin_User(models.Model):
    admin_user=models.OneToOneField(User,on_delete=models.CASCADE )
    phone=models.IntegerField()
    is_admin_user=models.BooleanField(default=True)
    def __str__(self):
        return self.admin_user.username

class Common_User(models.Model):
    common_user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone1=models.IntegerField()
    is_admin_user=models.BooleanField(default=False)

    def __str__(self):
        return self.common_user.username
    
class AndroidApp(models.Model):
    Appname = models.CharField(max_length=100)
    
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name