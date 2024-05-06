# Generated by Django 5.0.3 on 2024-05-05 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('sudokus', '0003_sudoku_solution_sudoku_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSudoku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('start', models.DateTimeField(auto_now=True)),
                ('duration', models.BigIntegerField(default=0)),
                ('hintsCount', models.IntegerField(default=0)),
                ('sudoku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sudokus.sudoku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ipaddressuser')),
            ],
        ),
    ]