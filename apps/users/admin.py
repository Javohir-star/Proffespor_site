from django.contrib import admin

from apps.users.models import User, Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "created_at"]
    search_fields = ["file"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "birth_date", "gender", "created_at"]
    search_fields = ["full_name"]