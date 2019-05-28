from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from contact.models import Person, Phone, Address, Email


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    radio_fields = {
        'role': admin.VERTICAL,
    }


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ['date_of_birth']
    autocomplete_fields = ['friends']
    list_display_links = ['first_name', 'last_name']
    search_fields = ['^last_name']
    list_display = ['last_name', 'first_name', 'date_of_birth', 'field_age']
    ordering = ['last_name', 'first_name']
    inlines = [AddressInline, PhoneInline, EmailInline]
    radio_fields = {
        'is_friend': admin.VERTICAL,
        'gender': admin.HORIZONTAL,
    }
    fieldsets = [
        (None, {
            'fields': ['last_name', 'first_name', 'is_friend']}),

        (_('Personal Data'), {
            'fields': ['pesel', 'date_of_birth', 'image', 'height', 'gender']}),

        (_('Other'), {
            'fields': ['homepage', 'notes', 'friends']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.modified_author = request.user

        if not change:
            # if object is created: change == True
            # if object is updated: change == False
            obj.add_author = request.user

        return super().save_model(request, obj, form, change)

    def field_age(self, model):
        return model.age()

    field_age.short_description = _('Age')
    field_age.admin_order_field = 'date_of_birth'
    field_age.default_if_none = 'n/a'

    class Media:
        js = [
            'contact/person.js',
        ]
        css = {'all': [
            'contact/person.css',
        ]}
