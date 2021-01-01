# Generated by Django 3.1.4 on 2020-12-30 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fragen',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('frage', models.TextField()),
                ('losung', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('numfra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesen.fragen')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('an', models.CharField(max_length=20)),
                ('numfra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesen.fragen')),
            ],
        ),
    ]
