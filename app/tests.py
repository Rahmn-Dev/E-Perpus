from django.test import TestCase

from django.urls import reverse
from app.models import buku, anggota, peminjaman
from django.contrib.auth.models import User
from app.forms import PeminjamanForm, BukuForm, AnggotaForm, MahasiswaForm
from app.serializers import BukuSerializer, AnggotaSerializer, PeminjamanSerializer

class BukuModelTestCase(TestCase):
    def test_create_buku(self):
        buku_obj = buku.objects.create(
            kode_buku='TEST123',
            judul_buku='Test Book',
            pengarang='Test Author',
            genre='Fantasy'
        )
        self.assertEqual(buku_obj.kode_buku, 'TEST123')
        self.assertEqual(buku_obj.judul_buku, 'Test Book')
        self.assertEqual(buku_obj.pengarang, 'Test Author')
        self.assertEqual(buku_obj.genre, 'Fantasy')
        print("Done buat  data buku [OK]")

    def test_edit_buku(self):
        buku_obj = buku.objects.create(
            kode_buku='TEST123',
            judul_buku='Test Book',
            pengarang='Test Author',
            genre='Fantasy'
        )
        updated_data = {
            'kode_buku': 'UPDATED123',
            'judul_buku': 'Updated Book',
            'pengarang': 'Updated Author',
            'genre': 'Updated Genre'
        }
        buku_obj.kode_buku = updated_data['kode_buku']
        buku_obj.judul_buku = updated_data['judul_buku']
        buku_obj.pengarang = updated_data['pengarang']
        buku_obj.genre = updated_data['genre']
        buku_obj.save()

        # Refresh the object from the database
        buku_obj.refresh_from_db()

        self.assertEqual(buku_obj.kode_buku, updated_data['kode_buku'])
        self.assertEqual(buku_obj.judul_buku, updated_data['judul_buku'])
        self.assertEqual(buku_obj.pengarang, updated_data['pengarang'])
        self.assertEqual(buku_obj.genre, updated_data['genre'])
        print("Done update  data  buku [OK]")

    def test_delete_buku(self):
        buku_obj = buku.objects.create(
            kode_buku='TEST123',
            judul_buku='Test Book',
            pengarang='Test Author',
            genre='Fantasy'
        )
        buku_id = buku_obj.id
        buku_obj.delete()

        with self.assertRaises(buku.DoesNotExist):
            buku.objects.get(id=buku_id)
        print("Done delete  data  buku [OK]")

class AnggotaModelTestCase(TestCase):
    def test_create_anggota(self):
        anggota_obj = anggota.objects.create(
            nim='12345',
            nama='Test Anggota',
            kelas='Test Kelas'
        )
        self.assertEqual(anggota_obj.nim, '12345')
        self.assertEqual(anggota_obj.nama, 'Test Anggota')
        self.assertEqual(anggota_obj.kelas, 'Test Kelas')
        print("Done buat  data  Anggota [OK]")

    def test_edit_anggota(self):
        anggota_obj = anggota.objects.create(
            nim='12345',
            nama='Test Anggota',
            kelas='Test Kelas'
        )
        updated_data = {
            'nim': '54321',
            'nama': 'Updated Anggota',
            'kelas': 'Updated Kelas'
        }
        anggota_obj.nim = updated_data['nim']
        anggota_obj.nama = updated_data['nama']
        anggota_obj.kelas = updated_data['kelas']
        anggota_obj.save()

        # Refresh the object from the database
        anggota_obj.refresh_from_db()

        self.assertEqual(anggota_obj.nim, updated_data['nim'])
        self.assertEqual(anggota_obj.nama, updated_data['nama'])
        self.assertEqual(anggota_obj.kelas, updated_data['kelas'])
        print("Done update  data  anggota [OK]")

    # def test_delete_anggota(self):
    #     anggota_obj = anggota.objects.create(
    #         nim='12345',
    #         nama='Test Anggota',
    #         kelas='Test Kelas'
    #     )
    #     anggota_id = anggota_obj.id
    #     anggota_obj.delete()

    #     with self.assertRaises(anggota.DoesNotExist):
    #         anggota.objects.get(id=anggota_id)

class PeminjamanModelTestCase(TestCase):
    def test_create_peminjaman(self):
        buku_obj = buku.objects.create(
            kode_buku='TEST123',
            judul_buku='Test Book',
            pengarang='Test Author',
            genre='Fantasy'
        )
        anggota_obj = anggota.objects.create(
            nim='12345',
            nama='Test Anggota',
            kelas='Test Kelas'
        )
        peminjaman_obj = peminjaman.objects.create(
            ticket='ABC123',
            nim=anggota_obj,
            nama=anggota_obj,
            buku=buku_obj,
            status='Dipinjam',
            tanggal_kembali=None
        )
        self.assertEqual(peminjaman_obj.ticket, 'ABC123')
        self.assertEqual(peminjaman_obj.nim, anggota_obj)
        self.assertEqual(peminjaman_obj.nama, anggota_obj)
        self.assertEqual(peminjaman_obj.buku, buku_obj)
        self.assertEqual(peminjaman_obj.status, 'Dipinjam')
        self.assertIsNone(peminjaman_obj.tanggal_kembali)
        print("Done buat  data Peminjam [OK]")

    def test_edit_peminjaman(self):
        buku_obj = buku.objects.create(
            kode_buku='TEST123',
            judul_buku='Test Book',
            pengarang='Test Author',
            genre='Fantasy'
        )
        anggota_obj = anggota.objects.create(
            nim='12345',
            nama='Test Anggota',
            kelas='Test Kelas'
        )
        peminjaman_obj = peminjaman.objects.create(
            ticket='ABC123',
            nim=anggota_obj,
            nama=anggota_obj,
            buku=buku_obj,
            status='Dipinjam',
            tanggal_kembali=None
        )
        updated_data = {
            'ticket': 'XYZ789',
            'nim': anggota_obj,
            'nama': anggota_obj,
            'buku': buku_obj,
            'status': 'Kembali',
            'tanggal_kembali': '2023-06-01'
        }
        peminjaman_obj.ticket = updated_data['ticket']
        peminjaman_obj.nim = updated_data['nim']
        peminjaman_obj.nama = updated_data['nama']
        peminjaman_obj.buku = updated_data['buku']
        peminjaman_obj.status = updated_data['status']
        peminjaman_obj.tanggal_kembali = updated_data['tanggal_kembali']
        peminjaman_obj.save()
        
        peminjaman_obj.refresh_from_db()

        self.assertEqual(peminjaman_obj.ticket, updated_data['ticket'])
        self.assertEqual(peminjaman_obj.nim, updated_data['nim'])
        self.assertEqual(peminjaman_obj.nama, updated_data['nama'])
        self.assertEqual(peminjaman_obj.buku, updated_data['buku'])
        self.assertEqual(peminjaman_obj.status, updated_data['status'])
        self.assertEqual(str(peminjaman_obj.tanggal_kembali), updated_data['tanggal_kembali'])
        print("Done edit  data  peminjam [OK]")

    def test_delete_peminjaman(self):
        buku_obj = buku.objects.create(
            kode_buku='TEST123',
            judul_buku='Test Book',
            pengarang='Test Author',
            genre='Fantasy'
        )
        anggota_obj = anggota.objects.create(
            nim='12345',
            nama='Test Anggota',
            kelas='Test Kelas'
        )
        peminjaman_obj = peminjaman.objects.create(
            ticket='ABC123',
            nim=anggota_obj,
            nama=anggota_obj,
            buku=buku_obj,
            status='Dipinjam',
            tanggal_kembali=None
        )
        peminjaman_id = peminjaman_obj.id
        peminjaman_obj.delete()

        with self.assertRaises(peminjaman.DoesNotExist):
            peminjaman.objects.get(id=peminjaman_id)
        print("Done hapus  data  peminjam [OK]")

class BukuSerializerTestCase(TestCase):
    def test_buku_serializer(self):
        buku_obj = buku.objects.create(
            kode_buku='TEST123',
            judul_buku='Test Book',
            pengarang='Test Author',
            genre='Fantasy'
        )
        serializer = BukuSerializer(buku_obj)
        expected_data = {
            'id': buku_obj.id,
            'kode_buku': 'TEST123',
            'judul_buku': 'Test Book',
            'pengarang': 'Test Author',
            'genre': 'Fantasy'
        }
        self.assertEqual(serializer.data, expected_data)
        print("Done test API buku create [OK]")



class AnggotaSerializerTestCase(TestCase):
    def test_anggota_serializer(self):
        anggota_obj = anggota.objects.create(
            nim='12345',
            nama='Test Anggota',
            kelas='Test Kelas'
        )
        serializer = AnggotaSerializer(anggota_obj)
        expected_data = {
            'id': anggota_obj.id,
            'nim': '12345',
            'nama': 'Test Anggota',
            'kelas': 'Test Kelas'
        }
        self.assertEqual(serializer.data, expected_data)
        print("Done test API Anggota create [OK]")

    def test_anggota_serializer_update(self):
        anggota_obj = anggota.objects.create(
            nim='12345',
            nama='Test Anggota',
            kelas='Test Kelas'
        )
        serializer = AnggotaSerializer(anggota_obj, data={'nama': 'Updated Anggota'})
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(serializer.data['nama'], 'Updated Anggota')
        print("Done test API Anggota Update [OK]")



# class PeminjamanSerializerTestCase(TestCase):
#     def test_peminjaman_serializer(self):
#         buku_obj = buku.objects.create(
#             kode_buku='TEST123',
#             judul_buku='Test Book',
#             pengarang='Test Author',
#             genre='Fantasy'
#         )
#         anggota_obj = anggota.objects.create(
#             nim='12345',
#             nama='Test Anggota',
#             kelas='Test Kelas'
#         )
#         peminjaman_obj = peminjaman.objects.create(
#             ticket='ABC123',
#             nim=anggota_obj,
#             nama=anggota_obj,
#             buku=buku_obj,
#             status='Dipinjam',
#             tanggal_kembali=None
#         )
#         serializer = PeminjamanSerializer(peminjaman_obj)
#         expected_data = {
#             'id': peminjaman_obj.id,
#             'ticket': 'ABC123',
#             'nim': {
#                 'id': anggota_obj.id,
#                 'nim': '12345',
#                 'nama': 'Test Anggota',
#                 'kelas': 'Test Kelas'
#             },
#             'buku': {
#                 'id': buku_obj.id,
#                 'kode_buku': 'TEST123',
#                 'judul_buku': 'Test Book',
#                 'pengarang': 'Test Author',
#                 'genre': 'Fantasy'
#             },
#             'status': 'Dipinjam',
#             'tanggal_pinjam': None  # Corrected field name to 'tanggal_pinjam'
#         }
#         self.assertEqual(serializer.data, expected_data)
