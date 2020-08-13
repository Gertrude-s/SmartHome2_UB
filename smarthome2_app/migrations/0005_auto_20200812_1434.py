# Generated by Django 2.2.13 on 2020-08-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome2_app', '0004_auto_20200810_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyModel',
            fields=[
                ('data', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='метка')),
                ('name', models.CharField(max_length=32, verbose_name='имя')),
                ('type', models.CharField(max_length=32, verbose_name='тип')),
            ],
            options={
                'verbose_name': 'ключ',
                'verbose_name_plural': 'ключи',
            },
        ),
        migrations.DeleteModel(
            name='RFIDTagModel',
        ),
    ]
