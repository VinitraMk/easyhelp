# Generated by Django 2.0.6 on 2018-06-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iden', models.IntegerField()),
                ('sertype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeofservice', models.CharField(max_length=50)),
                ('startdate', models.DateField()),
                ('nameofservice', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('seraddr', models.CharField(default=None, max_length=200)),
                ('avgrating', models.FloatField(default=0.0)),
                ('reviewcount', models.IntegerField(default=0)),
                ('serviceid', models.CharField(max_length=15)),
                ('owneremail', models.CharField(max_length=50)),
                ('servicemail', models.CharField(default=None, max_length=50)),
                ('servicephone', models.CharField(default=None, max_length=50)),
                ('websiteurl', models.CharField(default=None, max_length=2000)),
            ],
        ),
    ]
