# Generated by Django 4.2.1 on 2023-06-09 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_remove_anggota_fakultas_remove_anggota_jenis_kelamin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peminjaman',
            name='buku',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.buku'),
        ),
    ]
