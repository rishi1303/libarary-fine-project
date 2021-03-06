# Generated by Django 3.0.4 on 2020-04-10 04:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20200409_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='fine',
            name='cur_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fine',
            name='issue_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fine',
            name='book_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
