from django.contrib import admin

# Register your models here.
from next_app.models import Admin_User,Common_User,AndroidApp
# Register your models here.
admin.site.register(Admin_User)
admin.site.register(Common_User)

admin.site.register(AndroidApp)