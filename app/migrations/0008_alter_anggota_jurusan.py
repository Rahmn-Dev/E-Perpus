# Generated by Django 4.2.1 on 2023-05-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_anggota_jurusan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggota',
            name='jurusan',
            field=models.CharField(choices=[('Akuntasi', 'Akuntasi'), ('Manajemen', 'Manajemen'), ('Perdagangan Internasional', 'perdagangan Internasionak'), ('Informatika', 'Informatika'), ('Industri', 'Industri'), ('Informasi', 'Informasi'), ('Elektro', 'Elektro'), ('Mesin', 'Mesin'), ('Sipil', 'Sipil'), ('Jepang', 'Jepang'), ('Inggris', 'Inggris'), ('Desain Grafis', 'Desain Grafis'), ('Multimedia', 'Multimedia'), ('Perpustakaan Sains Informasi', 'Perpustakaan Sains Informasi'), ('Produksi Film Televisi', 'Produksi Film Televisi')], max_length=100),
        ),
    ]
