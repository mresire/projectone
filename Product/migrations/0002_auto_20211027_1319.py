# Generated by Django 3.2.8 on 2021-10-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commodity',
            options={'verbose_name_plural': 'Commodity'},
        ),
        migrations.AlterField(
            model_name='commodity',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
