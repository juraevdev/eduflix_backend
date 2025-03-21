from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        ("Role", {"fields": ("role",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("name", "email", "role", "password1", "password2"),
        }),
    )
    list_display = ("name", "email", "role", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "role")
    search_fields = ("name", "email", "role")
    ordering = ("email",)
