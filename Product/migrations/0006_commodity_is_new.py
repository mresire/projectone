# Generated by Django 3.2.8 on 2021-10-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_alter_commodity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='is_new',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
