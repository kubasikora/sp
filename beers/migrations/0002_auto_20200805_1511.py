# Generated by Django 3.0.7 on 2020-08-05 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loanedbeer',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='loanedbeer',
            name='loanee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loanees', to=settings.AUTH_USER_MODEL, verbose_name='Piwkobiorca'),
        ),
        migrations.AlterField(
            model_name='loanedbeer',
            name='loaner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loaners', to=settings.AUTH_USER_MODEL, verbose_name='Piwkodawca'),
        ),
    ]