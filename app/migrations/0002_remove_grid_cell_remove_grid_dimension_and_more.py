# Generated by Django 4.1.1 on 2022-09-27 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grid',
            name='cell',
        ),
        migrations.RemoveField(
            model_name='grid',
            name='dimension',
        ),
        migrations.DeleteModel(
            name='Dimension',
        ),
        migrations.DeleteModel(
            name='Grid',
        ),
    ]