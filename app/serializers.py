from rest_framework import serializers
from .models import buku, anggota, peminjaman

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = buku
        fields = '__all__'

class AnggotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = anggota
        fields = '__all__'

class PeminjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = peminjaman
        fields = '__all__'