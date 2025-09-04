from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Account,UserProfile
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        'first_name',
        'last_name',
        'username',
        'last_login',
        'date_joined',
        'is_active',
    )
    list_display_links = ('email','first_name','last_name') 
    read_only_fields = ('last_joined','date_joined')
    ordering = ("-date_joined",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile)
