# Generated by Django 3.1.5 on 2021-01-26 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_employer_categ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
