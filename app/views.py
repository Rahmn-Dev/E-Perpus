from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import peminjaman, anggota, buku
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .forms import (PeminjamanForm, BukuForm, AnggotaForm,MahasiswaForm)
from rest_framework import generics, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from django.urls import reverse
import pprint
from django.template.loader import render_to_string
from xhtml2pdf import pisa




def home(request):
    databuku = buku.objects.all()
    datapeminjam = peminjaman.objects.all()
    dataanggota = anggota.objects.all()
    totaldipinjam = datapeminjam.filter(status='Dipinjam').count()
    totaldikembalikan = datapeminjam.filter(status='Dikembalikan').count()
    
    pprint.pprint(dataanggota)
    context = {
        'bukus' : databuku,
        'anggotas' : dataanggota,
        'peminjams' : datapeminjam,
        'total_dipinjam' : totaldipinjam,
        'total_dikembalikan': totaldikembalikan,
    }
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'index_super.html', context)
        else:
            return render(request, 'index_auth.html', context)
    else:
        return render(request, 'index.html')

@login_required
def peminjaman_list(request):
    form = PeminjamanForm()
    if request.method == 'POST':
        form = PeminjamanForm(request.POST)
        if form.is_valid():
            # form = form.save(commit=False)
            form.save()
            return redirect('peminjaman_list')
        
    listpeminjaman = peminjaman.objects.all()
    
    search_query = request.GET.get('search')
    if search_query:
        listpeminjaman = listpeminjaman.filter(Q(ticket__icontains=search_query) | Q(nim__nim__icontains=search_query) | Q(nama__nama__icontains=search_query) | Q(buku__judul_buku__icontains=search_query) | Q(status__icontains=search_query) | Q(tanggal_pinjam__icontains=search_query)| Q(tanggal_kembali__icontains=search_query) )

    context ={
        'list': listpeminjaman,
        'form': form,
    }

    return render(request, 'peminjaman.html', context)

@login_required
def deletepeminjam(request, id):
    peminjams = peminjaman.objects.get(id=id)
    peminjams.delete()
    return HttpResponseRedirect(reverse('peminjaman_list'))

@login_required
def editpeminjam(request, id):
    editpeminjams = peminjaman.objects.get(id=id)
    pprint.pprint(editpeminjams)
    form = PeminjamanForm(request.POST or None, instance=editpeminjams)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('peminjaman_list')
    # else:
    #     form = BukuForm(instance=editbukus)
    context = {
        'edit': editpeminjams,
        'forms': form,
    }
    return render(request, 'editpeminjam.html', context)

@login_required
def cetak_pdf(request, id):
    peminjam = get_object_or_404(peminjaman, id=id)
    mahasiswas = peminjam.nama.mahasiswa
    context = {
        'cetakpeminjam': peminjam,
        'ditailmahasiswa': mahasiswas,
    }
    html_string = render_to_string('cetak_pdf.html', context=context)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cetak-peminjam.pdf"'
    
    pisa_status = pisa.CreatePDF(html_string, dest=response)
    if pisa_status.err:
        return HttpResponse('Error saat membuat PDF')
    
    return response

# @login_required
# def buku_tambah(request):
#     form = BukuForm()
#     if request.method == 'POST':
#         form = BukuForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.save()  
#     context = {
#         'form': form,
#     }
#     return render(request, 'buku_form.html', context)

@login_required
def aAnggota(request):
    anggota_form = AnggotaForm()
    mahasiswa_form = MahasiswaForm()
    
    if request.method == 'POST':
        anggota_form = AnggotaForm(request.POST)
        mahasiswa_form = MahasiswaForm(request.POST)
        
        if anggota_form.is_valid() and mahasiswa_form.is_valid():
            anggota_instance = anggota_form.save()
            mahasiswa_instance = mahasiswa_form.save(commit=False)
            mahasiswa_instance.id = anggota_instance.id  # Assign the same ID as the anggota instance
            mahasiswa_instance.save()
            return redirect('aAnggota')
    
    listanggota = anggota.objects.all()
    search_query = request.GET.get('search')
    
    if search_query:
        listanggota = listanggota.filter(Q(nim__icontains=search_query) | Q(nama__icontains=search_query) | Q(kelas__icontains=search_query) | Q(mahasiswa__jurusan__icontains=search_query) | Q(mahasiswa__jenis_kelamin__icontains=search_query) | Q(mahasiswa__tanggal_lahir__icontains=search_query) | Q(mahasiswa__fakultas__icontains=search_query))

    context = {
        'list': listanggota,
        'anggota_form': anggota_form,
        'mahasiswa_form': mahasiswa_form,
    }
        
    return render(request, 'anggota.html', context)


@login_required
def deleteanggota(request, id):
    anggotas = anggota.objects.get(id=id)
    anggotas.delete()
    return HttpResponseRedirect(reverse('aAnggota'))


@login_required
def editanggota(request, id):
    editanggotas = anggota.objects.get(id=id)
    anggota_form = AnggotaForm(instance=editanggotas)
    mahasiswa_form = MahasiswaForm(instance=editanggotas.mahasiswa)

    if request.method == 'POST':
        anggota_form = AnggotaForm(request.POST, instance=editanggotas)
        mahasiswa_form = MahasiswaForm(request.POST, instance=editanggotas.mahasiswa)

        if anggota_form.is_valid() and mahasiswa_form.is_valid():
            anggota_form.save()
            mahasiswa_form.save()
            return redirect('aAnggota')

    context = {
        'edit': editanggotas,
        'anggota_form': anggota_form,
        'mahasiswa_form': mahasiswa_form,
    }
    return render(request, 'editanggota.html', context)

@login_required
def buku_list(request):
    form = BukuForm()
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buku_list')
        else:
            return HttpResponse("Error")
    items = buku.objects.all()
    
    search_query = request.GET.get('search')
    if search_query:
        items = items.filter(Q(judul_buku__icontains=search_query) | Q(pengarang__icontains=search_query) | Q(genre__icontains=search_query) | Q(kode_buku__icontains=search_query))
    
    sort_by = request.GET.get('sort')
    if sort_by:
        items = items.order_by(sort_by)
    # paginator = Paginator(items, len(items))
    # page_number = request.GET.get('page')
    # page = paginator.get_page(page_number)
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'buku.html', context)

@login_required
def deletebuku(request, id):
    bukus = buku.objects.get(id=id)
    bukus.delete()
    return HttpResponseRedirect(reverse('buku_list'))

@login_required
def editbuku(request, id):
    editbukus = buku.objects.get(id=id)
    form = BukuForm(request.POST or None, instance=editbukus)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('buku_list')
    # else:
    #     form = BukuForm(instance=editbukus)
    context = {
        'edit': editbukus,
        'form': form,
    }
    return render(request, 'editbuku.html', context)
