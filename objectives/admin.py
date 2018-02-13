from django.contrib import admin

from .models import Objective


@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    pass
