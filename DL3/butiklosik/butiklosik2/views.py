from django.shortcuts import render,redirect
from . import models

# Pelanggan
def pelanggan(request) :
    allpelangganobj = models.pelanggan.objects.all()
    return render(request, 'pelanggan.html' , {
        "allpelangganobj" : allpelangganobj
    })

def createdatapelanggan(request) :
    if request.method == 'GET' :
        return render(request, 'createdatapelanggan.html')
    else :
        idpelanggan = request.POST['idpelanggan']
        nama = request.POST['nama']
        jeniskelamin = request.POST['jeniskelamin']
        nohandphone = request.POST['nohandphone']
        alamat = request.POST['alamat']

        newpelanggan = models.pelanggan(
            idpelanggan = idpelanggan,
            nama = nama,
            jeniskelamin = jeniskelamin,
            nohandphone = nohandphone,
            alamat = alamat
        ).save()
        return redirect('pelanggan')

def updatepelanggan(request,id):
    pelangganobj = models.pelanggan.objects.get(idpelanggan=id)
    if request.method == "GET":
        return render(request,'updatepelanggan.html', {
            'pelangganobj' : pelangganobj,
        })
    else:
        pelangganobj.nama = request.POST['nama']    
        pelangganobj.jeniskelamin = request.POST['jeniskelamin']  
        pelangganobj.alamat = request.POST['alamat']
        pelangganobj.nohandphone = request.POST['nohandphone']
        pelangganobj.save()
        return redirect('pelanggan')

def deletepelanggan(request,id):
    pelangganobj = models.pelanggan.objects.get(idpelanggan=id)
    pelangganobj.delete()
    return redirect('pelanggan')

# Charge
def charge(request) :
    allchargeobj = models.charge.objects.all()

    return render(request, 'charge.html' , {
        "allchargeobj" : allchargeobj
    })

def createdatacharge(request) :
    if request.method == 'GET' :
        return render(request, 'createdatacharge.html')
    else :
        idcharge = request.POST['idcharge']
        rinciancharge = request.POST['rinciancharge']
        jenischarge = request.POST['jenischarge']
        hargacharge = request.POST['hargacharge']

        newcharge = models.charge(
            idcharge = idcharge,
            rinciancharge = rinciancharge,
            jenischarge = jenischarge,
            hargacharge = hargacharge,
            
        ).save()
        return redirect('charge')

def updatecharge(request,id):
    chargeobj = models.charge.objects.get(idcharge=id)
    if request.method == "GET":
        return render(request,'updatecharge.html', {
            'allchargeobj' : chargeobj,
        })
    else:
        chargeobj.idcharge = request.POST['idcharge']
        chargeobj.rinciancharge = request.POST['rinciancharge']
        chargeobj.jenischarge = request.POST['jenischarge']
        chargeobj.hargacharge = request.POST['hargacharge']
        chargeobj.save()
        return redirect('charge')

def deletecharge(request,id):
    chargeobj = models.charge.objects.get(idcharge=id)
    chargeobj.delete()
    return redirect('charge')

# Owner
def owner(request) :
    allownerobj = models.owner.objects.all()

    return render(request, 'owner.html' , {
        "allownerobj" : allownerobj
    })

def createdataowner(request) :
    if request.method == 'GET' :
        return render(request, 'createdataowner.html')
    else :
        nama = request.POST['nama']
        jeniskelamin = request.POST['jeniskelamin']
        nohandphone = request.POST['nohandphone']
        alamat = request.POST['alamat']

        newowner = models.owner(
            nama = nama,
            jeniskelamin = jeniskelamin,
            nohandphone = nohandphone,
            alamat = alamat,
            
        ).save()
        return redirect('owner')

def updateowner(request,id):
    ownerobj = models.owner.objects.get(idowner=id)
    if request.method == "GET":
        return render(request,'updateowner.html', {
            'allowner' : ownerobj,
        })
    else:
        ownerobj.idowner = request.POST['idowner']
        ownerobj.nama = request.POST['nama']
        ownerobj.jeniskelamin = request.POST['jeniskelamin']
        ownerobj.nohp = request.POST['nohandphone']
        ownerobj.alamat = request.POST['alamat']
        ownerobj.save()
        return redirect('owner')

def deleteowner(request,id):
    ownerobj = models.owner.objects.get(idowner=id)
    ownerobj.delete()
    return redirect('owner')

# Pakaian
def pakaian(request) :
    allpakaianobj = models.pakaian.objects.all()

    return render(request, 'pakaian.html' , {
        "allpakaianobj" : allpakaianobj
    })

def createdatapakaian(request) :
    if request.method == 'GET' :
        return render(request, 'createdatapakaian.html')
    else :
        jenispakaian = request.POST['jenispakaian']
        ukuranpakaian = request.POST['ukuranpakaian']
        hargapakaian = request.POST['hargapakaian']
        konfirmasipakaian = request.POST['konfirmasipakaian']

        newpakaian = models.pakaian(
            jenispakaian = jenispakaian,
            ukuranpakaian = ukuranpakaian,
            hargapakaian = hargapakaian,
            konfirmasipakaian = konfirmasipakaian)
        newpakaian.save()
        return redirect('pakaian')

def updatepakaian(request,id):
    pakaianobj = models.pakaian.objects.get(idpakaian=id)
    if request.method == "GET":
        return render(request,'updatepakaian.html', {
            'pakaianobj' : pakaianobj,
        })
    else:
        pakaianobj.jenispakaian = request.POST['jenispakaian']
        pakaianobj.ukuranpakaian = request.POST['ukuranpakaian']
        pakaianobj.hargapakaian = request.POST['hargapakaian']
        pakaianobj.konfirmasipakaian = request.POST['konfirmasipakaian']
        pakaianobj.save()
        return redirect('pakaian')

def deletepakaian(request,id):
    pakaianobj = models.pakaian.objects.get(idpakaian=id)
    pakaianobj.delete()
    return redirect('pakaian')

# Peminjaman
def peminjaman(request):
    allpeminjamanobj = models.peminjaman.objects.all()
    return render (request, 'peminjaman.html', {
        'allpeminjamanobj' : allpeminjamanobj,
    })

def createdatapeminjaman(request):
    if request.method == "GET":
        return render(request,'createdatapeminjaman.html')
    else:
        # idpakaian = request.POST['idpakaian']
        # idpelanggan = request.POST['idpelanggan']
        # idowner = request.POST['idowner']
        tanggalsewa = request.POST['tanggalsewa']
        statuspeminjaman = request.POST['statuspeminjaman']
        lamasewa = request.POST['lamasewa']
        tanggalkembali = request.POST['tanggalkembali']

        newpeminjaman = models.peminjaman(
            # idpakaian = idpakaian,
            # idpelanggan = idpelanggan,
            # idowner = idowner,
            tanggalsewa = tanggalsewa,
            statuspeminjaman = statuspeminjaman,
            lamasewa = lamasewa,
            tanggalkembali = tanggalkembali,
        ).save()
        return redirect('peminjaman')

def updatepeminjaman(request,id):
    peminjamanobj = models.peminjaman.objects.get(idpeminjaman=id)
    if request.method == "GET":
        return render(request,'updatepeminjaman.html', {
            'peminjamanobj' : peminjamanobj,
        })
    else:
        peminjamanobj.tanggalsewa = request.POST['tanggalsewa']
        peminjamanobj.statuspeminjaman = request.POST['statuspeminjaman']
        peminjamanobj.lamasewa = request.POST['lamasewa']
        peminjamanobj.tanggalkembali = request.POST['tanggalkembali']
        peminjamanobj.save()
        return redirect('peminjaman')

def deletepeminjaman(request,id):
    peminjamanobj = models.peminjaman.objects.get(idpeminjaman=id)
    peminjamanobj.delete()
    return redirect('peminjaman')

# Detail Charge
def detailcharge(request):
    detailchargeobj = models.detailcharge.objects.all()
    return render (request, 'detailcharge.html', {
        'alldetailchargeobj' : detailchargeobj,
    })

def createdatadetailcharge(request):
    if request.method == "GET":
        return render(request,'createdatadetailcharge.html')
    else:
        # idpakaian = request.POST['idpakaian']
        # idpelanggan = request.POST['idpelanggan']
        # idowner = request.POST['idowner']
        iddetailcharge = request.POST['iddetailcharge']
        idpeminjaman = request.POST['idpeminjaman']
        idcharge = request.POST['idcharge']
        jumlahitemcharge = request.POST['jumlahitemcharge']

        newdetailcharge = models.detailcharge(
            # idpakaian = idpakaian,
            # idpelanggan = idpelanggan,
            # idowner = idowner,
            iddetailcharge = iddetailcharge,
            idpeminjaman = idpeminjaman,
            idcharge = idcharge,
            jumlahitemcharge = jumlahitemcharge,
        ).save()
        return redirect('detailcharge')

def updatedetailcharge(request,id):
    detailchargeobj = models.detailcharge.objects.get(iddetailcharge=id)
    if request.method == "GET":
        return render(request,'updatedetailcharge.html', {
            'detailchargeobj' : detailchargeobj,
        })
    else:
        detailchargeobj.iddetailcharge = request.POST['iddetailcharge']
        detailchargeobj.idpeminjaman = request.POST['idpeminjaman']
        detailchargeobj.idcharge = request.POST['idcharge']
        detailchargeobj.jumlahitemcharge = request.POST['jumlahitemcharge']
        detailchargeobj.save()
        return redirect('detailcharge')
