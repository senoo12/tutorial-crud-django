from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from bangunan.models import *

# Create your views here.
class TambahView(View):
    def post(self, request):
        if request.method == "POST":
            nama_produk = request.POST['nama_produk']
            kategori = request.POST['kategori']
            harga_beli = request.POST['harga_beli']
            harga_jual = request.POST['harga_jual']
            obj = Produk.objects.create(nama_produk=nama_produk, kategori=kategori, harga_beli=harga_beli, harga_jual=harga_jual)
        obj.save()
        return redirect('/')
    def get(self, request):
        return render(request, 'tambah.html')

class IndexView(View):
    def get(self, request):
        produk = Produk.objects.all()
        return render(request, 'index.html', {'produk': produk})

class UpdateView(View):
    def post(self, request, pk): 
        if request.method == "POST":
            obj = Produk.objects.get(pk=pk)
            obj.nama_produk = request.POST['nama_produk']
            obj.kategori = request.POST.get('kategori') 
            obj.harga_beli = request.POST['harga_beli']
            obj.harga_jual = request.POST['harga_jual']
        obj.save()
        return redirect('/')
    def get(self, request, pk):
        produk = Produk.objects.filter(pk=pk)
        return render(request, 'update.html', {'produk': produk})


class DeleteView(View):
    def post(self, request, pk):
        if request.method == "POST":
            obj = Produk.objects.get(pk=pk)
        obj.delete()
        return redirect('/')