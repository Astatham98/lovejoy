# Generated by Django 4.0 on 2021-12-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovejoy', '0009_alter_evaluation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='user',
            field=models.CharField(max_length=150),
        ),
    ]