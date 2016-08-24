from django.db import models
from django import forms
# Create your models here.
class Pelicula(models.Model):
    listaGenero=(
    ('Comedia','Comedia'),
    ('Romance','Romance'),
    ('Suspenso','Suspenso'),
    ('Drama','Drama'),
    ('Accion','Accion'),
    ('Terror','Terror'),
    )
    listaClasificacion=(
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('E','E'),
    )
    idPelicula= models.AutoField(primary_key=True)
    #idPelicula= models.CharField(max_length=5)
    titulo=  models.CharField(max_length=100)
    genero=  models.CharField(max_length=20,choices=listaGenero)
    clasificacion=  models.CharField(max_length=30,choices=listaClasificacion)
    director=  models.CharField(max_length=30)
    interpretes=  models.CharField(max_length=100)
    sinopsis=  models.TextField()
    imagenPortada=  models.ImageField(upload_to='static/images')
    nacionalidad=  models.CharField(max_length=20)
    anio=  models.CharField(max_length=30)
    duracion= models.CharField(max_length=30)
    def __str__(self):
        return self.titulo

class Sala(models.Model):
    listaTipoSala=(
    ('Sala3d','Sala3d'),
    ('SalaHD','SalaHD'),
    ('SalaNormal','SalaNormal'),
    )
    idSala=models.AutoField(primary_key=True)
    NumSala= models.CharField(max_length=5)
    NumAsientos= models.IntegerField()
    TipoDeSala= models.CharField(max_length=20,choices=listaTipoSala)
    def __str__(self):
        return self.NumSala

class Sesion(models.Model):
    idSesion= models.AutoField(primary_key=True)
    NumSesion=models.CharField(max_length=5)
    fecha= models.DateTimeField()
    PrecioPorAsiento= models.FloatField()
    AsientosLibres= models.IntegerField()
    AsientosVendidos= models.IntegerField()
    def __str__(self):
        return self.NumSesion

class SalaSesion(models.Model):
    id_Sala= models.ForeignKey(Sala,on_delete=models.CASCADE,default="")
    id_Sesion= models.ForeignKey(Sesion,on_delete=models.CASCADE,default="")
    idSalaSesion= models.AutoField(primary_key=True)
