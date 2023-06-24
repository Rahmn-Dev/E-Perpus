
from rest_framework import generics, viewsets, permissions
from django_filters import rest_framework as filters

from .models import buku, anggota, peminjaman
from .serializers import BukuSerializer, AnggotaSerializer, PeminjamanSerializer

class BukuViewSet(viewsets.ModelViewSet):
    queryset = buku.objects.all()
    serializer_class = BukuSerializer
    
    def perform_create(self, serializer):
        super().perform_create(serializer)
    # filter_backends = (filters.BaseFilterBackend,)
    # search_fields = ('kode_buku','judul_buku','pengarang','genre',)
    
class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = anggota.objects.all()
    serializer_class = AnggotaSerializer
    
    def perform_create(self, serializer):
        super().perform_create(serializer)
    # filter_backends = (filters.BaseFilterBackend,)
    # search_fields = ('nim','nama','kelas','fakultas','jurusan','jenis_kelamin',)

class PeminjamanViewSet(viewsets.ModelViewSet):
    queryset = peminjaman.objects.all()
    serializer_class = PeminjamanSerializer
    
    def perform_create(self, serializer):
        super().perform_create(serializer)
    # filter_backends = (filters.BaseFilterBackend,)
    # search_fields = ('nim','nama','buku','status',)
    
    # def filter_queryset(self, queryset):
    #     filterset = self.get_filterset()
    #     if filterset:
    #         queryset = filterset.qs 
    #     return queryset