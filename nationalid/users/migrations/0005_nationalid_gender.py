# Generated by Django 3.1.8 on 2021-04-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_nationalid_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationalid',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]