from django.db import models
from django.urls import reverse
import random,string
import datetime as dt

class buku(models.Model):

    GENRE_CHOICES = (
        ('Fantasy','Fantasy'),
        ('Fantasy fiction','Fantasy fiction'),
        ('Science fiction','Science fiction'),
        ('English fiction','English fiction'),
        ('Adventure stories','Adventure stories'),
        ('True Crime','True Crime'),
        ('Education','Education'),
        ('Social Science','Social Science'),
        ('Business & Economics','Business & Economics'),
        ('Horror','Horror'),
        ('Philosophy','Philosophy'),
        ('Paranormal','Paranormal'),
        ('Historical fiction','Historical fiction'),
        ('Science','Science'),
        ("Children's stories","Children's stories"),
        ('Authors','Authors'),
        ('Juvenile Fiction','Juvenile Fiction'),
        ('Art','Art'),
        ('Self-Help','Self-Help'),
        ('Family & Relationships','Family & Relationships'),
        ('Sports & Recreation','Sports & Recreation'),
        ('Health & Fitness','Health & Fitness'),
        ('History','History'),
        ('Travel','Travel'),
        ('Humor','Humor'),
        ('Families','Families'),
        ('Animals','Animals'),
        ('Fiction','Fiction'),
        ('Religion','Religion'),
        ('Psychology','Psychology'),
        ('Biography & Autobiography','Biography & Autobiography'),
        ('Detective and mystery stories','Detective and mystery stories'),
    )

    kode_buku = models.CharField(max_length=120, blank=False, null=False)
    judul_buku = models.TextField(max_length=120, blank=False, null=False)
    pengarang = models.TextField(max_length=120, blank=False, null=False)
    genre = models.TextField(max_length=120, choices=GENRE_CHOICES)

    class Meta:
        pass
    def __str__(self):
            return f"{self.judul_buku} ({self.kode_buku})"



class anggota(models.Model):
    
    nim = models.CharField(max_length=100, blank=False, null=False,  unique=True)
    nama = models.CharField(max_length=100, blank=False, null=False,  unique=True)
    kelas = models.CharField(max_length=100, blank=False, null=False)


    class Meta:
        pass
        
    def __str__(self):
        return f"{self.nama} ({self.nim})"
    
class mahasiswa(anggota):
    FAKULTAS_CHOICES = (
    ('EKONOMI DAN BISNIS', 'EKONOMI DAN BISNIS'),
    ('TEKNIK', 'TEKNIK'),
    ('ILMU BUDAYA', 'ILMU BUDAYA'),
    ('DESAIN KOMUNIKASI DAN VISUAL', 'DESAIN KOMUNIKASI DAN VISUAL'),
    )
    JURUSAN_CHOICES = (
        ('Akuntasi' , 'Akuntasi'),
        ('Manajemen', 'Manajemen'),
        ('Perdagangan Internasional', 'perdagangan Internasional'),
        ('Informatika', 'Informatika'),
        ('Industri', 'Industri'),
        ('Informasi', 'Informasi'),
        ('Elektro', 'Elektro'),
        ('Mesin', 'Mesin'),
        ('Sipil', 'Sipil'),
        ('Jepang', 'Jepang'),
        ('Inggris', 'Inggris'),
        ('Desain Grafis', 'Desain Grafis'),
        ('Multimedia', 'Multimedia'),
    )
    JENIS_KELAMIN_CHOICES = (
        ('Laki-Laki' , 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    )
    fakultas = models.CharField(max_length=100, choices=FAKULTAS_CHOICES)
    jurusan = models.TextField(max_length=100, choices=JURUSAN_CHOICES)
    jenis_kelamin = models.TextField( choices=JENIS_KELAMIN_CHOICES, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    def __str__(self):
        return f"{self.fakultas} ({self.jurusan})"
    
# class dosen(anggota):
    

class peminjaman(models.Model):
    STATUS_CHOICES = (
        ('Dipinjam' , 'Dipinjam'),
        ('Dikembalikan' , 'Dikembalikan'),
    )
    def randomless():
        N = 12
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        return res
    randomless()
    
    ticket = models.CharField(max_length=12, default=randomless)
    nim = models.ForeignKey(anggota, on_delete=models.CASCADE, related_name='peminjaman_nim', to_field='nim')
    nama = models.ForeignKey(anggota, on_delete=models.CASCADE, related_name='peminjaman_nama', to_field='nama')
    buku = models.OneToOneField(buku,  on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, blank=False, null=False)
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_kembali = models.DateField(null=True, blank=True)

    class Meta:
        pass
    
    def __str__(self):
            return f"{self.ticket} {self.anggotamhs()} {self.yangdipinjam()}  {self.tanggal_kembali}"
    
    def anggotamhs(self):
            return f" {self.nim} {self.nama}"
        
    def yangdipinjam(self):
            return f" {self.buku} {self.status}"
