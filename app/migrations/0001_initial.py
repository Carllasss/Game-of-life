# Generated by Django 4.1.1 on 2022-09-26 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cells')),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dimension')),
            ],
        ),
    ]
