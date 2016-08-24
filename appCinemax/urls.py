from django.conf.urls import url
from django.contrib import admin
from appCinemax.views import ListarUsuario,ModificarUsuario,CrearUsuario,inicioAdmin
from appCinemax.views import ListarPelicula,ModificarPelicula,IngresarPelicula,VerSalas
from appCinemax.views import IngresarSala,ModificarSala,VerSesion,IngresarSesion,ModificarSesion
from appCinemax.views import VerSalaSesion,IngresarSalaSesion,ModificarSalaSesion,listPelicula
urlpatterns=[
	url(r'^listarU/',ListarUsuario, name="ListarUsuario"),
    url(r'^modificarU/',ModificarUsuario,name="ModificarUsuario"),
    url(r'^crearU/',CrearUsuario,name="CrearUsuario"),
	url(r'^$',inicioAdmin,name="inicioAdmin"),
	url(r'^listarP/',ListarPelicula,name="ListarPelicula"),
	url(r'^modificarP/',ModificarPelicula,name="ModificarPelicula"),
    url(r'^ingresarP/',IngresarPelicula,name="IngresarPelicula"),
	url(r'^verS/',VerSalas,name="VerSalas"),
	url(r'^ingresarS/',IngresarSala,name="IngresarSala"),
	url(r'^modificarS/',ModificarSala,name="ModificarSala"),
	url(r'^verSe/',VerSesion,name="VerSesion"),
	url(r'^ingresarSe/',IngresarSesion,name="IngresarSesion"),
	url(r'^modificarSe/',ModificarSesion,name="ModificarSesion"),
	url(r'^verSaSe/',VerSalaSesion,name="VerSalaSesion"),
	url(r'^ingresarSaSe/',IngresarSalaSesion,name="IngresarSalaSesion"),
	url(r'^modificarSaSe/',ModificarSalaSesion,name="ModificarSalaSesion"),
	url(r'^listPWS/',listPelicula,name="listPelicula"),

]
