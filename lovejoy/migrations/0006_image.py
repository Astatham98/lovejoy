# Generated by Django 4.0 on 2021-12-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovejoy', '0005_evaluation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
