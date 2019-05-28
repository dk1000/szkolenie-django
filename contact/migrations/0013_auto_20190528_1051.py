# Generated by Django 2.2.1 on 2019-05-28 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0012_person_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='add_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='add_author', to=settings.AUTH_USER_MODEL, verbose_name='Add Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='modified_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modified_author', to=settings.AUTH_USER_MODEL, verbose_name='Modified Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Add Date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified Date'),
        ),
    ]