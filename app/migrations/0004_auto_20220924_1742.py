# Generated by Django 3.2 on 2022-09-24 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220924_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start', models.DateField(verbose_name='Sprint Start')),
                ('end', models.DateField(verbose_name='Sprint End')),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='sprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sprint'),
        ),
        migrations.AddField(
            model_name='initiative',
            name='sprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.Model, to='app.sprint'),
        ),
    ]
