# Generated by Django 3.2 on 2022-09-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_initiative_squad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='backend_dev',
            field=models.IntegerField(default=0, verbose_name='BE'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='business_analysts',
            field=models.IntegerField(default=0, verbose_name='BA'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='frontend_dev',
            field=models.IntegerField(default=0, verbose_name='FE'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='qa_engineer',
            field=models.IntegerField(default=0, verbose_name='QA'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='scrum_master',
            field=models.IntegerField(default=0, verbose_name='SM'),
        ),
    ]