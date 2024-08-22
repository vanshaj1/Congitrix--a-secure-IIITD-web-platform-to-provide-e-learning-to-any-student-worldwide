from django.contrib import admin

# Register your models here.
from .models import allCourses,allInstructors
admin.site.register(allCourses)
admin.site.register(allInstructors)