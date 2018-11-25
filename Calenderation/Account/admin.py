from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.admin import TokenAdmin

from .forms import ChroniclerRegistrationForm, UserChangeForm
from .models import Chronicler


class ChroniclerAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = ChroniclerRegistrationForm
    list_display = ('email_address', 'name', 'birth_date', 'created_date', 'is_active')
    list_display_links = ('email_address',)
    list_filter = ('is_superuser', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email_address', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser',)}),

    )
    add_fieldsets = (
        (None, {
            'fields': ('email_address', 'name', 'birth_date', 'password1', 'password2')
        }),
    )
    search_fields = ('email_address', 'name')
    ordering = ('is_active', 'is_superuser')
    filter_horizontal = ()

TokenAdmin.raw_id_fields = ('user',)
admin.site.register(Chronicler, ChroniclerAdmin)
