# Generated by Django 4.0.2 on 2022-04-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='image',
            field=models.ImageField(upload_to='mobileimages/'),
        ),
    ]