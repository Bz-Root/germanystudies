# Generated by Django 3.1.4 on 2020-12-20 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('datedenaissance', models.CharField(default='02-01-2002', max_length=50)),
                ('username', models.CharField(max_length=18)),
                ('telephone', models.CharField(default='0652518306', max_length=18)),
                ('datecreationaccount', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Succes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('succes_schreiben', models.IntegerField()),
                ('succes_lesen', models.IntegerField()),
                ('succes_horen', models.IntegerField()),
                ('succes_grammar', models.IntegerField()),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.user')),
            ],
        ),
    ]
