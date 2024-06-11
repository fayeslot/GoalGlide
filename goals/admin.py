from django.contrib import admin
from .models import  Goal

# Register your models here.



class GoalAdmin(admin.ModelAdmin):
  list_display = ("name", "status", "target_date",)
  prepopulated_fields = {"slug": ("name",)}


admin.site.register(Goal, GoalAdmin)

