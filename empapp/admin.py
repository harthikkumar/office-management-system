from django.contrib import admin
from .models import Person,Role,Department
# Register your models here.

admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Department)