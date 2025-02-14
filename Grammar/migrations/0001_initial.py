# Generated by Django 3.1.4 on 2021-01-12 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frage', models.CharField(max_length=200)),
                ('losung', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valide', models.BooleanField(default=False)),
                ('pers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pers', to='Auth.personne')),
                ('ubung', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Grammar.ubung')),
            ],
        ),
        migrations.CreateModel(
            name='Essai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(max_length=15)),
                ('numf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grammar.ubung')),
            ],
        ),
    ]
