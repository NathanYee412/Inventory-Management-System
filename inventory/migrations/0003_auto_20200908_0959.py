# Generated by Django 3.1.1 on 2020-09-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200908_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='partNumber',
            field=models.CharField(default='PART NUMBER', max_length=20),
        ),
        migrations.AddField(
            model_name='equipment',
            name='partNumber',
            field=models.CharField(default='PART NUMBER', max_length=20),
        ),
        migrations.AddField(
            model_name='laptop',
            name='partNumber',
            field=models.CharField(default='PART NUMBER', max_length=20),
        ),
        migrations.AddField(
            model_name='mobile',
            name='partNumber',
            field=models.CharField(default='PART NUMBER', max_length=20),
        ),
    ]