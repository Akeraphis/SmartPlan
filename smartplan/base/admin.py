from django.contrib import admin
from .models import Company, DataLayer, DataTable, Profile

# Register your models here.
admin.site.register(Company)
admin.site.register(DataLayer)
admin.site.register(DataTable)
admin.site.register(Profile)