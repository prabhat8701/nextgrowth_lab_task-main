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
    
APP_CATEGORIES = [
    ('Entertaiment', 'Entertaiment 1'),
    ('category2', 'Category 2'),
    # Add more categories as needed
]

SUB_CATEGORIES = [
    ('sub_category1', 'Sub Category 1'),
    ('sub_category2', 'Sub Category 2'),
    # Add more sub-categories as needed
]

class AndroidApp(models.Model):
    Appname = models.CharField(max_length=100)
    Applink = models.URLField()
    App_category = models.CharField(max_length=50, choices=APP_CATEGORIES, default='category1')
    Sub_category = models.CharField(max_length=50, choices=SUB_CATEGORIES, default='sub_category1')
    App_img = models.ImageField(upload_to='App_img/')
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.Appname



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
