# Generated by Django 4.0.5 on 2022-06-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked'), ('eliminated', 'Eliminated')], default='active', max_length=10, verbose_name='Estado'),
        ),
    ]
