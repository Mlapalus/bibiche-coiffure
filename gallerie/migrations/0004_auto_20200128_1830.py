# Generated by Django 3.0.2 on 2020-01-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallerie', '0003_auto_20200128_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myphotomodel',
            name='image',
            field=models.ImageField(upload_to='gallerie'),
        ),
    ]
