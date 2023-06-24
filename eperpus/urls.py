from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from app import views
from app.api import  (
   
#     BukuListCreateAPIView,
#     BukuRetrieveUpdateDestroyAPIView,
#     AnggotaListCreateAPIView,
#     AnggotaRetrieveUpdateDestroyAPIView,
#     PeminjamanListCreateAPIView,
#     PeminjamanRetrieveUpdateDestroyAPIView,
    BukuViewSet,
    AnggotaViewSet,
    PeminjamanViewSet,

)
router = DefaultRouter()
router.register(r'buku', BukuViewSet)
router.register(r'anggota', AnggotaViewSet)
router.register(r'peminjaman', PeminjamanViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/buku/', BukuListCreateAPIView.as_view(), name='buku-list'),
    # path('api/v1/buku/<int:pk>/', BukuRetrieveUpdateDestroyAPIView.as_view(), name='buku-detail'),
    # path('api/v1/anggota/', AnggotaListCreateAPIView.as_view(), name='anggota-list'),
    # path('api/v1/anggota/<int:pk>/', AnggotaRetrieveUpdateDestroyAPIView.as_view(), name='anggota-detail'),
    # path('api/v1/peminjaman/', PeminjamanListCreateAPIView.as_view(), name='peminjaman-list'),
    # path('api/v1/peminjaman/<int:pk>/', PeminjamanRetrieveUpdateDestroyAPIView.as_view(), name='peminjaman-detail'),
    #API
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('listpeminjam/', views.peminjaman_list, name='peminjaman_list'),
    path('listpeminjam/delete/<int:id>', views.deletepeminjam, name='deletepeminjam'),
    path('listpeminjam/cetak/<int:id>', views.cetak_pdf, name='cetak_pdf'),
    path('listpeminjam/edit/<int:id>', views.editpeminjam, name='editpeminjam'),
    path('listanggota/', views.aAnggota, name='aAnggota'),
    path('listanggota/delete/<int:id>', views.deleteanggota, name='deleteanggota'),
    path('listanggota/edit/<int:id>', views.editanggota, name='editanggota'),
    # path('addbuku/', views.buku_tambah, name='buku'),
    path('listbuku/', views.buku_list, name='buku_list'),
    path('listbuku/delete/<int:id>', views.deletebuku, name='deletebuku'),
    path('listbuku/edit/<int:id>', views.editbuku, name='editbuku'),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='changepassword.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
