from django.contrib import admin

# Register your models here.
from Tables.models import Table, BookTime

admin.site.register(Table)
admin.site.register(BookTime)
