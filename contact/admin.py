from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from contact.models import Person, Phone, Address, Email


admin.site.site_header = _('Addressbook')
admin.site.index_title = _('Dashboard')
admin.site.site_title = _('Addressbook')
# admin.site.index_template = 'admin/dashboard.html'


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
    list_display = ['last_name', 'first_name', 'field_pesel', 'date_of_birth', 'field_age', 'field_born_in_fifties']
    ordering = ['last_name', 'first_name']
    inlines = [AddressInline, PhoneInline, EmailInline]
    radio_fields = {
        'is_friend': admin.VERTICAL,
        'gender': admin.HORIZONTAL}
    fieldsets = [
        (None, {'fields': ['last_name', 'first_name', 'is_friend']}),
        (_('Personal Data'), {'fields': ['pesel', 'date_of_birth', 'image', 'height', 'gender']}),
        (_('Other'), {'fields': ['homepage', 'notes', 'friends']})]

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
    field_age.empty_value_display = 'n/a'

    def field_born_in_fifties(self, model):
        if model.date_of_birth:
            return model.date_of_birth.strftime('%Y')[:3] == '195'

    field_born_in_fifties.boolean = True

    def field_pesel(self, model):
        if model.pesel:
            return format_html(f'<span style="color: #f00;">{model.pesel}</span>')
        else:
            return None

    field_pesel.admin_order_field = 'first_name'
    field_pesel.empty_value_display = ''

    class Media:
        js = [
            'contact/person.js',
        ]
        css = {'all': [
            'contact/person.css',
        ]}
