# Generated by Django 3.2.5 on 2021-08-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='batman_pujagj.png', upload_to=''),
        ),
    ]
