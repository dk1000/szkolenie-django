# Generated by Django 2.2.1 on 2019-05-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20190528_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='homepage',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='Homepage'),
        ),
    ]
