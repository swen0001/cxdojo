from django.contrib import admin
from .models import MyUser, Files


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "username",
        "date_joined",
    )


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):

    list_display = (
        "file_csv",
        "uploaded",
        "activated",
    )
    list_display_links = (
        "file_csv",
        "uploaded",
    )
