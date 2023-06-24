from django.contrib import admin
from .models import buku, peminjaman, anggota

class bukuAdmin(admin.ModelAdmin):
    list_display = ['kode_buku', 'judul_buku', 'pengarang', 'genre']
    list_filter = ['genre']
    search_fields = ['kode_buku', 'judul_buku', 'pengarang', 'genre']

class anggotaAdmin(admin.ModelAdmin):
    list_display = ['nim', 'nama', 'kelas', ]
    list_filter = ['nama']
    search_fields = ['nim', 'nama', 'kelas', ]

admin.site.register(buku, bukuAdmin)
admin.site.register(peminjaman)
admin.site.register(anggota, anggotaAdmin)
