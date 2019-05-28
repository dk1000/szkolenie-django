from datetime import datetime
from typing import Optional
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    HEIGHT_MIN = 100
    HEIGHT_MAX = 220

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_UNSPECIFIED = None
    GENDER_CHOICES = [
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
        (GENDER_UNSPECIFIED, _('Unspecified'))]

    first_name = models.CharField(verbose_name=_('First Name'), max_length=30)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=30)
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'), blank=True, null=True, default=None)
    pesel = models.PositiveIntegerField(verbose_name=_('PESEL'), help_text=_('Type your PESEL number'), blank=True, null=True, default=None)
    image = models.ImageField(verbose_name=_('Image'), upload_to='image/', blank=True, null=True, default=None)
    homepage = models.URLField(verbose_name=_('Homepage'), blank=True, null=True, default=None)
    notes = models.TextField(verbose_name=_('Notes'), blank=True, null=True, default=None)
    height = models.DecimalField(verbose_name=_('Height'), max_digits=4, decimal_places=1, validators=[MinValueValidator(HEIGHT_MIN), MaxValueValidator(HEIGHT_MAX)], blank=True, null=True, default=None)
    gender = models.CharField(verbose_name=_('Gender'), max_length=30, choices=GENDER_CHOICES, blank=True, null=True, default=None)

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
