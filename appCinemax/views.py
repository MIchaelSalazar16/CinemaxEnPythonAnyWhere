from django.shortcuts import redirect,render
from .models import Sala,Pelicula,Sesion,SalaSesion
from .forms import FormularioPelicula,FormularioSala,FormularioSesion,FormularioSalaSesion
from django.core.files.uploadedfile import SimpleUploadedFile
import json as simplejson
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers

# Create your views here.
def inicioAdmin(request):
    p=Pelicula.objects.all()
    context={
    'p':p,
    }
    return render(request,"InicioAdmin.html",context)

def InfoPelicula(request):
    p=Pelicula.objects.get(idPelicula=request.GET['idPelicula'])
    context={
    'p':p,
    }
    return render(request,"InfoPelicula.html",context)

def ListarPelicula(request):
    peli= Pelicula.objects.all()
    context={
    'p':peli,
    }
    return render(request,"ListarPeliculas.html",context)

def IngresarPelicula(request):
    f= FormularioPelicula(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if f.is_valid():
            datos= f.cleaned_data
            p=Pelicula()
            p.titulo=datos.get("titulo")
            p.genero=datos.get("genero")
            p.clasificacion=datos.get("clasificacion")
            p.director=datos.get("director")
            p.interpretes=datos.get("interpretes")
            p.sinopsis=datos.get("sinopsis")
            p.imagenPortada=datos.get("imagenPortada")
            p.anio=datos.get("anio")
            p.duracion=datos.get("duracion")
            if p.save() != True:
                return redirect(ListarPelicula)
    context={'f':f,}
    return render(request,"IngresarPeliculas.html",context)

def ModificarPelicula(request):
    f = FormularioPelicula(request.POST or None,request.FILES or None)
    p = Pelicula.objects.get(idPelicula=request.GET['idPelicula'])
    f.fields["titulo"].initial=p.titulo
    f.fields["genero"].initial=p.genero
    f.fields["clasificacion"].initial=p.clasificacion
    f.fields["director"].initial=p.director
    f.fields["interpretes"].initial=p.interpretes
    f.fields["sinopsis"].initial=p.sinopsis
    f.fields["imagenPortada"].initial=p.imagenPortada
    f.fields["anio"].initial=p.anio
    f.fields["duracion"].initial=p.duracion
    if request.method == 'POST':
        if f.is_valid():
            datos= f.cleaned_data
            p.titulo=datos.get("titulo")
            p.genero=datos.get("genero")
            p.clasificacion=datos.get("clasificacion")
            p.director=datos.get("director")
            p.interpretes=datos.get("interpretes")
            p.sinopsis=datos.get("sinopsis")
            p.imagenPortada=datos.get("imagenPortada")
            p.anio=datos.get("anio")
            p.duracion=datos.get("duracion")
            if p.save() != True:
                return redirect(ListarPelicula)
    context={
        'f':f,
        'p':p,
    }
    return render(request,"ModificarPeliculas.html",context)

def VerSalas(request):
    sala= Sala.objects.all()
    context={
    's':sala,
    }
    return render(request,"VerSalas.html",context)

def IngresarSala(request):
    f= FormularioSala(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if f.is_valid():
            datos= f.cleaned_data
            s=Sala()
            #s.idSala=datos.get("dSala")
            s.NumSala=datos.get("NumSala")
            s.NumAsientos=datos.get("NumAsientos")
            s.TipoDeSala=datos.get("TipoDeSala")
            if s.save() != True:
                return redirect(VerSalas)
    context={'f':f,}
    return render(request,"IngresarSalas.html",context)

def ModificarSala(request):
    f = FormularioSala(request.POST or None)
    s = Sala.objects.get(idSala=request.GET['idSala'])
    #f.fields['idSala'].initial= s.idSala
    f.fields['NumSala'].initial=s.NumSala
    f.fields['NumAsientos'].initial=s.NumAsientos
    f.fields['TipoDeSala'].initial= s.TipoDeSala
    if request.method == 'POST':
        if f.is_valid():
            datos= f.cleaned_data
            #s.idSala=datos.get("idSala")
            s.NumSala=datos.get("NumSala")
            s.NumAsientos=datos.get("NumAsientos")
            s.TipoDeSala=datos.get("TipoDeSala")
            if s.save() != True:
                return redirect(VerSalas)
    context={
        'f':f,
        's':s,
    }
    return render(request,"ModificarSalas.html",context)

def VerSesion(request):
    sesion= Sesion.objects.all()
    context={
    's':sesion,
    }
    return render(request,"VerSesion.html",context)

def IngresarSesion(request):
    f= FormularioSesion(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if f.is_valid():
            datos= f.cleaned_data
            s=Sesion()
            s.NumSesion=datos.get("NumSesion")
            s.fecha=datos.get("fecha")
            s.PrecioPorAsiento=datos.get("PrecioPorAsiento")
            s.AsientosLibres=datos.get("AsientosLibres")
            s.AsientosVendidos=datos.get("AsientosVendidos")
            if s.save() != True:
                return redirect(VerSesion)
    context={'f':f,}
    return render(request,"IngresarSesion.html",context)

def ModificarSesion(request):
    f = FormularioSesion(request.POST or None)
    s = Sesion.objects.get(idSesion=request.GET['idSesion'])
    f.fields['NumSesion'].initial=s.NumSesion
    f.fields['fecha'].initial=s.fecha
    f.fields['PrecioPorAsiento'].initial=s.PrecioPorAsiento
    f.fields['AsientosLibres'].initial= s.AsientosLibres
    f.fields['AsientosVendidos'].initial= s.AsientosVendidos
    if request.method == 'POST':
        if f.is_valid():
            datos= f.cleaned_data
            s.NumSesion=datos.get("NumSesion")
            s.fecha=datos.get("fecha")
            s.PrecioPorAsiento=datos.get("PrecioPorAsiento")
            s.AsientosLibres=datos.get("AsientosLibres")
            s.AsientosVendidos=datos.get("AsientosVendidos")
            if s.save() != True:
                return redirect(VerSesion)
    context={
        'f':f,
        's':s,
    }
    return render(request,"ModificarSesion.html",context)

def VerSalaSesion(request):
    f= SalaSesion.objects.all()
    context={
    'f':f,
    }
    return render(request,"VerSalaSesion.html",context)

def IngresarSalaSesion(request):
    f= FormularioSalaSesion(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if f.is_valid():
            datos= f.cleaned_data
            s=SalaSesion()
            s.id_Sala=datos.get("id_Sala")
            s.id_Sesion=datos.get("id_Sesion")
            if s.save() != True:
                return redirect(VerSalaSesion)
    context={'f':f,}
    return render(request,"IngresarSalaSesion.html",context)

def ModificarSalaSesion(request):
    f = FormularioSalaSesion(request.POST or None)
    s = SalaSesion.objects.get(idSalaSesion=request.GET['idSalaSesion'])
    #f.fields['idSalaSesion'].initial=s.idSalaSesion
    f.fields['id_Sala'].initial=s.id_Sala
    f.fields['id_Sesion'].initial=s.id_Sesion
    if request.method == 'POST':
        if f.is_valid():
            datos= f.cleaned_data
            s.id_Sala=datos.get("id_Sala")
            s.id_Sesion=datos.get("id_Sesion")
            if s.save() != True:
                return redirect(VerSalaSesion)
    context={
        'f':f,
        's':s,
    }
    return render(request,"ModificarSalaSesion.html",context)

def listPelicula(request):
    peliculas = Pelicula.objects.all() #Modelo del que van a sacar el json
    mresult = []
    mreturn = {}
    for m in peliculas:
        mresult.append({"movie":m.titulo,
                        "tagline":m.genero,
                        "rating":m.clasificacion,
                        "director":m.director,
                        "cast":m.interpretes,
                        "story":m.sinopsis,
                        #"image":m.imagenPortada,
                        "year":m.anio,
                        "duration":m.duracion})
    mreturn['movies'] = mresult
    return HttpResponse(simplejson.dumps(mreturn),'application/json')

def SesionAsignada(request):
    s=Sesion.objects.get(NumSesion=request.GET['NumSesion'])
    context={
    's':s,
    }
    return render(request,"SesionAsignada.html",context)

def SalaAsignada(request):
    s=Sala.objects.get(NumSala=request.GET['NumSala'])
    context={
    's':s,
    }
    return render(request,"SalaAsignada.html",context)
