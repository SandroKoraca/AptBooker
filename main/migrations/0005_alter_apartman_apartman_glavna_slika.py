# Generated by Django 4.1 on 2022-09-01 10:41

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_apartman_apartman_glavna_slika'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartman',
            name='apartman_glavna_slika',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.image_path),
        ),
    ]
