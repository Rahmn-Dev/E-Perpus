from django import forms
from .models import peminjaman, buku, anggota, mahasiswa

class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = peminjaman
        fields = ('ticket', 'nim', 'nama', 'buku', 'status', 'tanggal_kembali')

class BukuForm(forms.ModelForm):
    class Meta:
        model = buku
        fields = ('kode_buku', 'judul_buku', 'pengarang', 'genre')

class AnggotaForm(forms.ModelForm):
    class Meta:
        model = anggota
        fields = ('nim', 'nama', 'kelas')

class MahasiswaForm(AnggotaForm):
  
    class Meta(AnggotaForm.Meta):
        model = mahasiswa
        fields = AnggotaForm.Meta.fields + ('fakultas', 'jurusan', 'jenis_kelamin', 'tanggal_lahir')