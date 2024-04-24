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
    Applink =
    App_category=
    Sub_category=
    App_imge= models.ImageField(upload_to='App_img/')
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name



# user_app/models.py
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)
    tasks_completed = models.PositiveIntegerField(default=0)
    # Add more fields as per your requirements (e.g., profile picture, etc.)

    def __str__(self):
        return self.user.username
    

# user_app/models.py
class TaskScreenshot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=200)
    screenshot_img = models.ImageField(upload_to='task_screenshots/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.task_description}"
