# Generated by Django 3.0.2 on 2020-01-28 16:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallerie', '0002_auto_20200128_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='myphotomodel',
            name='date_creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de creation'),
        ),
        migrations.AddField(
            model_name='myphotomodel',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myphotomodel',
            name='titre',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
