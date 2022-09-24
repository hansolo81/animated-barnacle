# Generated by Django 3.2 on 2022-09-24 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('scrum_master', models.IntegerField(null=True, verbose_name='SM')),
                ('business_analysts', models.IntegerField(null=True, verbose_name='BA')),
                ('frontend_dev', models.IntegerField(null=True, verbose_name='FE')),
                ('backend_dev', models.IntegerField(null=True, verbose_name='BE')),
                ('qa_engineer', models.IntegerField(null=True, verbose_name='QA')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.domain')),
            ],
        ),
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('planned_for', models.DateField(verbose_name='Planned For')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.domain')),
                ('squad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.squad')),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='tribe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tribe'),
        ),
    ]
