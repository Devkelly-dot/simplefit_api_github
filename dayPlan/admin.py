from django.contrib import admin

from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Dayplan)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Food)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Cardio)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Lift)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Log)
class AuthorAdmin(admin.ModelAdmin):
    pass
