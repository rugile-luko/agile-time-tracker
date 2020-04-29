from django.contrib import admin
from . import models

admin.site.register(models.Developer)
admin.site.register(models.Sprint)
admin.site.register(models.Story)
admin.site.register(models.Task)
admin.site.register(models.TimeSpent)
