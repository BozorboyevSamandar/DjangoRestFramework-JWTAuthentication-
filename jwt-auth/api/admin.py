from django.contrib import admin
from .models import Student

# Register your models here.


admin.site.register(Student)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'address')
