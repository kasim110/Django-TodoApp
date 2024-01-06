from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'created_at', 'is_active')

    fieldsets = (
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'mobile', 'email', 'password','city','state','country','zipcode','address')}),
        (_('Permissions'), {'fields': ('is_admin', 'is_staff', 'is_active', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'created_at')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('mobile',)
    filter_horizontal = ('groups',)
    readonly_fields = ('created_at',)