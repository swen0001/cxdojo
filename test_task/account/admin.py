from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import User


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'avatar',
                ),
            },
        ),
    )

    def user_avatar(self, obj):
        return format_html('<img src="{}" width="75" height="70" style="border-radius: 50%" />'.format(obj.avatar))

    list_display = (
        "user_avatar",
        "username",
        "email",
        "is_staff",
    )
    list_display_links = (
        "user_avatar",
        "username",
        "email",
    )


admin.site.register(User, CustomUserAdmin)
