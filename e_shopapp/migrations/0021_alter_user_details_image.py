# Generated by Django 4.0.1 on 2022-04-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shopapp', '0020_alter_user_details_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='image',
            field=models.ImageField(default='shop/user_profile_default_image/user_profile_default_image.png', upload_to='media/shop/user_profile_images'),
        ),
    ]
