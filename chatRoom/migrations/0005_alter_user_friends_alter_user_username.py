# Generated by Django 4.1 on 2023-01-09 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatRoom', '0004_alter_user_friends_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(to='chatRoom.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]