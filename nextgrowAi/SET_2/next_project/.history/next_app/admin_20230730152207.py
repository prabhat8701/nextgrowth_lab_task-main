from django.contrib import admin

# Register your models here.
from next_app.models import Admin_User,Common_User
# Register your models here.

admin.site.register(Admin_User)
admin.site.register(Teacher)