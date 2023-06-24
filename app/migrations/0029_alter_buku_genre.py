# Generated by Django 4.2.1 on 2023-05-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_buku_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='genre',
            field=models.TextField(choices=[('Fantasy', 'Fantasy'), ('Adventure stories', 'Adventure stories'), ('True Crime', 'True Crime'), ('Contemporary', 'Contemporary'), ('Dystopian', 'Dystopian'), ('Business & Economics', 'Business & Economics'), ('Horror', 'Horror'), ('Philosophy', 'Philosophy'), ('Paranormal', 'Paranormal'), ('Historical fiction', 'Historical fiction'), ('Science', 'Science'), ("Children's stories", "Children's stories"), ('Authors', 'Authors'), ('Juvenile Fiction', 'Juvenile Fiction'), ('Art', 'Art'), ('Self-Help', 'Self-Help'), ('Family & Relationships', 'Family & Relationships'), ('Motivational', 'Motivational'), ('History', 'History'), ('Travel', 'Travel'), ('Humor', 'Humor'), ('Families', 'Families'), ('Guide', 'Guide'), ('Fiction', 'Fiction'), ('Religion', 'Religion'), ('Psychology', 'Psychology'), ('Biography & Autobiography', 'Biography & Autobiography'), ('Juvenile Fiction', 'Juvenile Fiction'), ('Detective and mystery stories', 'Detective and mystery stories')], max_length=120),
        ),
    ]
