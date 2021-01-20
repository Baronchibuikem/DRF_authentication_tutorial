from django.contrib import admin
from app_accounts.models import CustomUser, Role


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name",
                    "email",)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Role)
