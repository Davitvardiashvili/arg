# Generated by Django 4.1.5 on 2023-05-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movement', '0003_alter_gallery_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='user.png', upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='title',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.ImageField(default='user.png', upload_to='images'),
        ),
    ]
