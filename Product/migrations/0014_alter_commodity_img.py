# Generated by Django 3.2.8 on 2021-11-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_alter_commodity_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='media/images'),
        ),
    ]
