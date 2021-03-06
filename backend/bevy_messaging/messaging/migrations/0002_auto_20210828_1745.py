# Generated by Django 3.2.6 on 2021-08-28 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='message',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='read_at',
        ),
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='is_recieved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Sent at'),
        ),
    ]
