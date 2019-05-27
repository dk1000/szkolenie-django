from datetime import datetime
from typing import Optional
from pathlib import Path
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=30)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=30)
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'), blank=True, null=True, default=None)
    pesel = models.PositiveIntegerField(verbose_name=_('PESEL'), blank=True, null=True, default=None)
    avatar = models.ImageField(verbose_name=_('Avatar'), upload_to='avatar/', blank=True, null=True, default=None)

    def age(self) -> Optional[int]:
        if not self.date_of_birth:
            return None

        age = datetime.now().date() - self.date_of_birth
        return round(age.days / settings.YEAR)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
