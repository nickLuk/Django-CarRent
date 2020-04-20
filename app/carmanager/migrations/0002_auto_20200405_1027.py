# Generated by Django 3.0.4 on 2020-04-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmanager',
            name='phone1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='carmanager',
            name='phone2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='carmanager',
            name='phone3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='carmanager',
            name='position',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='carmanager',
            name='telegram',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='carmanager',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]