# Generated by Django 3.1.1 on 2020-09-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcmback', '0002_auto_20200919_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblusuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='tblusuario',
            name='scoreActivity',
            field=models.IntegerField(default=0),
        ),
    ]
