# Generated by Django 3.0.7 on 2020-08-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifarank', '0003_auto_20200804_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='inPKs',
            field=models.BooleanField(default=False, verbose_name='Po karnych'),
        ),
    ]