# Generated by Django 4.2.1 on 2023-05-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_anggota_jurusan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggota',
            name='jurusan',
            field=models.CharField(choices=[('Akuntasi', 'Akuntasi'), ('Manajemen', 'Manajemen'), ('Perdagangan Internasional', 'perdagangan Internasionak'), ('Informatika', 'Informatika'), ('Industri', 'Industri'), ('Informasi', 'Informasi'), ('Elektro', 'Elektro'), ('Mesin', 'Mesin'), ('Sipil', 'Sipil'), ('Jepang', 'Jepang'), ('Inggris', 'Inggris'), ('Desain Grafis', 'Desain Grafis'), ('Multimedia', 'Multimedia'), ('Perpustakaansains', 'PerpustakaanSainsInformasi'), ('ProduksiFilmTelevisi', 'ProduksiFilmTelevisi')], max_length=100),
        ),
    ]
