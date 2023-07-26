from django.db import models

# Create your models here.
class Produk(models.Model):
    C = 'Cat'   #menandakan choice dalam django
    S = 'Semen'
    G = 'Gypsum'

    kategori = (
        (C, C),
        (S, S),
        (G, G),
    )

    nama_produk = models.CharField(max_length=30)
    kategori = models.CharField(max_length=10, choices=kategori, default=S)
    harga_beli = models.IntegerField(max_length=20)
    harga_jual = models.IntegerField(max_length=20)
