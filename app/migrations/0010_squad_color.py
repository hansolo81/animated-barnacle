# Generated by Django 3.2 on 2022-09-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_member_manday_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='color',
            field=models.CharField(default='green', max_length=20),
            preserve_default=False,
        ),
    ]