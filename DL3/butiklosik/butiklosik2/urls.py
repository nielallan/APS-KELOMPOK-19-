from django.urls import path
from . import views

urlpatterns = [
    path('pelanggan',views.pelanggan, name='pelanggan'),
    path('createdatapelanggan',views.createdatapelanggan, name='createdatapelanggan'),
    path('updatepelanggan/<str:id>', views.updatepelanggan,name='updatepelanggan'),
    path('deletepelanggan/<str:id>', views.deletepelanggan,name='deletepelanggan'),
    path('charge',views.charge, name='charge'),
    path('createdatacharge',views.createdatacharge, name='createdatacharge'),
    path('updatecharge/<str:id>',views.updatecharge,name='updatecharge'),
    path('deletecharge/<str:id>',views.deletecharge,name='deletecharge'),
    path('owner',views.owner, name='owner'),
    path('createdataowner',views.createdataowner, name='createdataowner'),
    path('updateowner/<str:id>',views.updateowner,name='updateowner'),
    path('deleteowner/<str:id>',views.deleteowner,name='deleteowner'),
    path('pakaian',views.pakaian, name='pakaian'),
    path('createdatapakaian',views.createdatapakaian, name='createdatapakaian'),
    path('updatepakaian/<str:id>',views.updatepakaian,name='updatepakaian'),
    path('deletepakaian/<str:id>',views.deletepakaian,name='deletepakaian'),
    path('peminjaman', views.peminjaman,name='peminjaman'),
    path('createdatapeminjaman',views.createdatapeminjaman,name='createdatapeminjaman'),
    path('updatepeminjaman/<str:id>', views.updatepeminjaman,name='updatepeminjaman'),
    path('deletepeminjaman/<str:id>', views.deletepeminjaman,name='deletepeminjaman'),
     path('detailcharge', views.detailcharge,name='detailcharge'),
    path('createdatadetailcharge',views.createdatadetailcharge,name='createdatadetailcharge'),
    path('updatedetailcharge/<str:id>', views.updatedetailcharge,name='updatedetailcharge'),
    
]
