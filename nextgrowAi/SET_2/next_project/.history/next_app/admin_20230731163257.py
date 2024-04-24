from django.contrib import admin

# Register your models here.
from next_app.models import Admin_User,Common_User,AndroidApp,UserProfile,TaskScreenshot
# Register your models here.
admin.site.register(Admin_User)
admin.site.register(Common_User)

admin.site.register(AndroidApp)
admin.site.register(UserProfile)
TaskScreenshot

