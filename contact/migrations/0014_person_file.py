# Generated by Django 2.2.1 on 2019-05-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_auto_20190528_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='files/', verbose_name='File'),
        ),
    ]
