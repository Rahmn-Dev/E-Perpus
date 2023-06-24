# Generated by Django 4.2.1 on 2023-05-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_buku_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='genre',
            field=models.TextField(choices=[('Fantasy', 'Fantasy'), ('Adventure', 'Adventure'), ('Romance', 'Romance'), ('Contemporary', 'Contemporary'), ('Dystopian', 'Dystopian'), ('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Thriller', 'Thriller'), ('Paranormal', 'Paranormal'), ('Historical fiction', 'Historical fiction'), ('Science Fiction', 'Science Fiction'), ('Childrens', 'Childrens'), ('Memoir', 'Memoir'), ('Cookbook', 'Cookbook'), ('Art', 'Art'), ('Self-Help', 'Self-Help'), ('Development', 'Development'), ('Motivational', 'Motivational'), ('History', 'History'), ('Travel', 'Travel'), ('Humor', 'Humor'), ('Families', 'Families'), ('Guide', 'Guide'), ('Fiction', 'Fiction'), ('Religion', 'Religion'), ('Psychology', 'Psychology'), ('Biography & Autobiography', 'Biography & Autobiography'), ('Juvenile Fiction', 'Juvenile Fiction')], max_length=120),
        ),
    ]