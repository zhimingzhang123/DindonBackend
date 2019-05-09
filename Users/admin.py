from django.contrib import admin

# Register your models here.
from Users.models import User

admin.site.register(User)
