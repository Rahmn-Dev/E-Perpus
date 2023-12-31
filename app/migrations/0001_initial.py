# Generated by Django 4.2.1 on 2023-05-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=100)),
                ('kelas', models.CharField(max_length=100)),
                ('fakultas', models.CharField(choices=[('EKONOMI DAN BISNIS', 'EKONOMI DAN BISNIS'), ('TEKNIK', 'TEKNIK'), ('ILMU BUDAYA', 'ILMU BUDAYA'), ('DESAIN KOMUNIKASI DAN VISUAL', 'DESAIN KOMUNIKASI DAN VISUAL'), ('ILMU SOSIAL DAN POLITIK', 'ILMU SOSIAL DAN POLITIK')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_buku', models.CharField(max_length=100)),
                ('judul_buku', models.CharField(max_length=100)),
                ('pengarang', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('Fantasy', 'Fantasy'), ('Adventure', 'Adventure'), ('Romance', 'Romance'), ('Contemporary', 'Contemporary'), ('Dystopian', 'Dystopian'), ('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Thriller', 'Thriller'), ('Paranormal', 'Paranormal'), ('Historical fiction', 'Historical fiction'), ('Science Fiction', 'Science Fiction'), ('Childrens', 'Childrens'), ('Memoir', 'Memoir'), ('Cookbook', 'Cookbook'), ('Art', 'Art'), ('Self-help', 'Self-help'), ('Development', 'Development'), ('Motivational', 'Motivational'), ('History', 'History'), ('Travel', 'Travel'), ('Humor', 'Humor'), ('Families', 'Families'), ('Guide', 'Guide')], max_length=100)),
            ],
        ),
    ]
