from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import UserCreationForm, UserChangeForm
from.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets+((
        None, {'fields': ('age',)}),
                                     )
    add_fieldsets = UserAdmin.add_fieldsets+(
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)




