from django.contrib import admin
from django.utils.html import format_html

from .models import MyUser, Files


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "username",
        "date_joined",
    )
    list_display_links = (
        "first_name",
        "last_name",
        "username",
    )


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):

    list_display = (
        "file_csv",
        "file_xml",
        "uploaded",
        "activated",
    )
    list_display_links = (
        "file_csv",
        "file_xml",
        "uploaded",
    )
