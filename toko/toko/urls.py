from bangunan.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tambah/', TambahView.as_view(), name='tambah'),
    path('', IndexView.as_view(), name='index'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete')
]
