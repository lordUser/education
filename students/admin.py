from django.contrib import admin
from .models import Student, StudentGroup

class StudentInlineAdmin(admin.TabularInline):
    model = Student


class StudentGroupAdmin(admin.ModelAdmin):
    inlines = [StudentInlineAdmin,]


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentGroup, StudentGroupAdmin)
