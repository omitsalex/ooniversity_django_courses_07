from django.contrib import admin
from courses.models import *

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Student)  # Register your models here.
