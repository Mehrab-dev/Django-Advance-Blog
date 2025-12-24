from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User , Profile


class CustomUserAdmin(UserAdmin) :
    model = User
    list_display = ['email','is_superuser','is_staff','is_active']
    list_filter = ['is_superuser','is_active']
    search_fields = ['email']
    ordering = ('email',)

    fieldsets = (
        ('Authentication',{
            'fields':('email','password')
        }),
        ('Permission',{
            'fields':('is_superuser','is_staff','is_active')
        }),
        ('Group Permission',{
            'fields':('groups','user_permissions')
        }),
        ('important date',{
            'fields':('last_login',)
        }),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide'),
            'fields':('email','password1','password2','is_superuser','is_staff','is_active'),
        }),
    )



admin.site.register(Profile)
admin.site.register(User,CustomUserAdmin)