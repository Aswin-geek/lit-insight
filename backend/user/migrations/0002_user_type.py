# Generated by Django 5.0.2 on 2024-03-12 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(default='user', max_length=10),
            preserve_default=False,
        ),
    ]
