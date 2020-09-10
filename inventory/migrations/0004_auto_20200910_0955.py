# Generated by Django 3.1.1 on 2020-09-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200908_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='serviceTag',
            field=models.CharField(default='SERVICE TAG', max_length=20),
        ),
        migrations.AddField(
            model_name='equipment',
            name='serviceTag',
            field=models.CharField(default='SERVICE TAG', max_length=20),
        ),
        migrations.AddField(
            model_name='laptop',
            name='serviceTag',
            field=models.CharField(default='SERVICE TAG', max_length=20),
        ),
        migrations.AddField(
            model_name='mobile',
            name='serviceTag',
            field=models.CharField(default='SERVICE TAG', max_length=20),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='issues',
            field=models.CharField(default='ENTER ISSUES', max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='issues',
            field=models.CharField(default='ENTER ISSUES', max_length=100),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='issues',
            field=models.CharField(default='ENTER ISSUES', max_length=100),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='issues',
            field=models.CharField(default='ENTER ISSUES', max_length=100),
        ),
    ]