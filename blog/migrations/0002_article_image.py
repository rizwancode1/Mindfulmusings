# Generated by Django 4.2.4 on 2023-08-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='Featured_image.jpg', null=True, upload_to=''),
        ),
    ]
