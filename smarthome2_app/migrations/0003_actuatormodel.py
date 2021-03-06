# Generated by Django 2.2.13 on 2020-08-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome2_app', '0002_auto_20200806_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActuatorModel',
            fields=[
                ('channel', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='канал')),
                ('time_sent', models.DateTimeField(verbose_name='отправлено')),
                ('value', models.FloatField(verbose_name='значение')),
            ],
            options={
                'verbose_name': 'исполнитель',
                'verbose_name_plural': 'исполнители',
                'ordering': ['time_sent'],
                'get_latest_by': 'time_sent',
            },
        ),
    ]
