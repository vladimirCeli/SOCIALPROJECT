# Generated by Django 3.2.5 on 2021-08-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_alter_relationship_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/dzkcr9eec/image/upload/v1/media/man_tfyuzb', upload_to=''),
        ),
    ]
