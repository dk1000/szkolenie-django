from django.db import models
from django.utils.translation import gettext_lazy as _


class Email(models.Model):
    ROLE_HOME = 'home'
    ROLE_WORK = 'work'
    ROLE_OTHER = 'other'
    ROLE_CHOICES = [
        (ROLE_WORK, _('Work')),
        (ROLE_HOME, _('Home')),
        (ROLE_OTHER, _('Other'))]

    person = models.ForeignKey(verbose_name=_('Person'), to='contact.Person', on_delete=models.CASCADE)
    role = models.CharField(verbose_name=_('Role'), max_length=30, choices=ROLE_CHOICES, default=ROLE_OTHER)
    email = models.EmailField(verbose_name=_('Number'), unique=True)

    def __str__(self) -> str:
        return f'{self.person} {self.email} ({self.role})'

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')
