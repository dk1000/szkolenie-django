from django.db import models
from django.utils.translation import gettext_lazy as _


class Phone(models.Model):
    ROLE_HOME = 'home'
    ROLE_WORK = 'work'
    ROLE_MOBILE = 'mobile'
    ROLE_CHOICES = [
        (ROLE_WORK, _('Work')),
        (ROLE_HOME, _('Home')),
        (ROLE_MOBILE, _('Mobile'))]

    person = models.ForeignKey(verbose_name=_('Person'), to='contact.Person', on_delete=models.CASCADE)
    role = models.CharField(verbose_name=_('Role'), max_length=30, choices=ROLE_CHOICES, default=ROLE_MOBILE)
    number = models.CharField(verbose_name=_('Number'), max_length=20, unique=True)

    def __str__(self) -> str:
        return f'{self.person} {self.number} ({self.role})'

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')
