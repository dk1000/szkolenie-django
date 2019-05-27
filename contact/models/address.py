from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    ROLE_HOME = 'home'
    ROLE_WORK = 'work'
    ROLE_OTHER = 'other'
    ROLE_CHOICES = [
        (ROLE_WORK, _('Work')),
        (ROLE_HOME, _('Home')),
        (ROLE_OTHER, _('Other'))]

    person = models.ForeignKey(verbose_name=_('Person'), to='contact.Person', on_delete=models.CASCADE)
    role = models.CharField(verbose_name=_('Role'), max_length=30, choices=ROLE_CHOICES, default=ROLE_HOME)
    street = models.CharField(verbose_name=_('Street'), max_length=30, blank=True, null=True, default=None)
    house_number = models.CharField(verbose_name=_('House Number'), max_length=30, blank=True, null=True, default=None)
    apartment = models.CharField(verbose_name=_('Apartment'), max_length=30, blank=True, null=True, default=None)
    post_code = models.CharField(verbose_name=_('Post Code'), max_length=30, blank=True, null=True, default=None)
    city = models.CharField(verbose_name=_('City'), max_length=30, blank=True, null=True, default=None)
    state = models.CharField(verbose_name=_('State'), max_length=30, blank=True, null=True, default=None)
    country = models.CharField(verbose_name=_('Country'), max_length=30, blank=True, null=True, default=None)

    def __str__(self) -> str:
        return f'{self.person} {self.street} {self.city}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
