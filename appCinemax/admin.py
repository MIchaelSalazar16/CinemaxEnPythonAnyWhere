from django.contrib import admin
from .models import Usuario
from .models import Pelicula
from .models import Sala
from .models import SalaSesion
from .models import Sesion
# Register your models here.
class AdminUsuario(admin.ModelAdmin):
	list_display=["__str__","nombres","apellidos","clave"]
	list_editable=["nombres","apellidos","clave"]
	list_filter=["clave"]
	search_fields=["__str__","nombres","apellidos"]

	class Meta:
		model= Usuario

admin.site.register(Usuario,AdminUsuario)

class AdminPelicula(admin.ModelAdmin):
	list_display=["__str__","titulo","genero","clasificacion","director","interpretes","sinopsis","imagenPortada","nacionalidad","anio","duracion"]
	list_editable=["titulo","genero","clasificacion","director","interpretes","sinopsis","imagenPortada","nacionalidad","anio","duracion"]
	list_filter=["titulo","genero"]
	search_fields=["titulo","genero"]

	class Meta:
		model= Pelicula

admin.site.register(Pelicula,AdminPelicula)

class AdminSala(admin.ModelAdmin):
	list_display=["idSala","NumSala","NumAsientos","TipoDeSala"]
	list_editable=["NumSala","NumAsientos","TipoDeSala"]
	list_filter=["idSala"]
	search_fields=["idSala","__str__"]

	class Meta:
		model= Sala

admin.site.register(Sala,AdminSala)

class AdminSesion(admin.ModelAdmin):
	list_display=["idSesion","NumSesion","fecha","PrecioPorAsiento","AsientosLibres","AsientosVendidos"]
	list_editable=["NumSesion","fecha","PrecioPorAsiento","AsientosLibres","AsientosVendidos"]
	list_filter=["AsientosLibres"]
	search_fields=["idSesion"]

	class Meta:
		model= Sesion

admin.site.register(Sesion,AdminSesion)

class AdminSalaSesion(admin.ModelAdmin):
	list_display=["idSalaSesion","id_Sala","id_Sesion"]
	search_fields=["idSalaSesion"]
	list_filter=["idSalaSesion"]
	search_fields=["idSalaSesion"]

	class Meta:
		model= SalaSesion

admin.site.register(SalaSesion,AdminSalaSesion)
