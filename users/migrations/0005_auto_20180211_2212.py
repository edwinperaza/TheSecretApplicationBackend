# Generated by Django 2.0.2 on 2018-02-12 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
        ('languages', '0001_initial'),
        ('users', '0004_auto_20170919_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='birthday'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='countries_plus.Country', verbose_name='country'),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='languages.Language', verbose_name='language'),
        ),
    ]
