# Generated by Django 3.2.7 on 2024-03-08 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='billtbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wid', models.CharField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='complainttbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=150)),
                ('date', models.DateTimeField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='paymenttbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=100)),
                ('wid', models.CharField(max_length=100)),
                ('cardtype', models.CharField(max_length=100)),
                ('cardname', models.CharField(max_length=100)),
                ('cardno', models.CharField(max_length=100)),
                ('cvv', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userregg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('place', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='wrkregg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('place', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='assigntbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wname', models.CharField(max_length=150)),
                ('wid', models.CharField(max_length=150)),
                ('uname', models.CharField(max_length=300)),
                ('time', models.DateTimeField(max_length=300)),
                ('status', models.CharField(max_length=100)),
                ('cstatus', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=100)),
                ('cmpltid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esm.complainttbl')),
            ],
        ),
    ]
