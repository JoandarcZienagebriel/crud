from django.contrib import admin
from .models import Point, GradeTen

class PointAdmin(admin.ModelAdmin):
    list_display=[
        'author',
        "name",
        "chemistry",
        "biology",
        "math",
        'physics'
    ]

class GradeTenAdmin(admin.ModelAdmin):
    list_display=[
        'author',
        "name",
        "chemistry",
        "biology",
        "math",
        'physics'
    ]

admin.site.register(Point, PointAdmin)
admin.site.register(GradeTen, GradeTenAdmin)
# Register your models here.
