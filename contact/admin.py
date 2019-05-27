from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from contact.models import Person, Phone, Address


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    radio_fields = {
        'role': admin.VERTICAL,
    }


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ['date_of_birth']
    list_display_links = ['first_name', 'last_name']
    search_fields = ['^last_name']
    list_display = ['last_name', 'first_name', 'date_of_birth', 'field_age']
    ordering = ['last_name', 'first_name']
    inlines = [AddressInline, PhoneInline]
    fieldsets = [
        (None, {
            'fields': ['last_name', 'first_name']}),

        (_('Personal Data'), {
            'fields': ['pesel', 'date_of_birth']}),
    ]

    def field_age(self, model):
        return str(model.age())

    field_age.short_description = _('Age')
    field_age.admin_order_field = 'date_of_birth'


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    autocomplete_fields = ['person']
    radio_fields = {
        'role': admin.VERTICAL
    }
