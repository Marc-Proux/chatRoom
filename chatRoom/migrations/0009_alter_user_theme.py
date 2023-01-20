# Generated by Django 4.1 on 2023-01-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatRoom', '0008_alter_user_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='theme',
            field=models.IntegerField(choices=[('light', 'Light'), ('dark', 'Dark')], default='dark'),
        ),
    ]