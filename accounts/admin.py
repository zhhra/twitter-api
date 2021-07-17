from django.contrib import admin
from .models.user import User
from django.contrib.auth.admin import UserAdmin


UserAdmin.fieldsets[1][1]["fields"] += (
    "sex",
    "phone_number",
    "birth_date",
    "followings",
)


UserAdmin.list_display += (
    "username",
    "first_name",
    "last_name",
    "followings_count",
    "followers_count",
)


UserAdmin.list_filter += ("sex", "birth_date")

UserAdmin.search_fields += ("birth_date",)

admin.site.register(User, UserAdmin)
