from django.db import models

#Instalar PIL para las imagenes

class Auditoria(models.Model):
	ACTIVO = 'ACT'
	INACTIVO = 'INA'
	ESTADO_CHOISES = (
		(ACTIVO, 'Activo'),
		(INACTIVO, 'Inactivo'),
		)
	usuario_new = models.CharField(max_length=30)
	fecha_new = models.DateField(auto_now_add=True)
	usuario_mod = models.CharField(max_length=30, blank=True)
	fecha_mod = models.DateField(blank=True, null=True)
	estado = models.CharField(max_length=3, choices=ESTADO_CHOISES, default=ACTIVO)
    
	class Meta:
		abstract = True
	
	def is_upperclass(self):
		return self.estado in (self.ACTIVO, self.INACTIVO)

	

class Rol(Auditoria):
	nombre = models.CharField(max_length=50, verbose_name=u'Descripcion Rol')

	def __unicode__(self):
		return self.nombre

class Genero(Auditoria):
	descripcion = models.CharField(max_length=30, verbose_name=u'Genero')

	def __unicode__(self):
		return self.descripcion


class Persona(Auditoria):
	dni = models.CharField(max_length=8, primary_key=True, verbose_name=u'Nro DNI')
	primer_nombre = models.CharField(max_length=15, verbose_name=u'Nombre Principal')
	otros_nombre = models.CharField(max_length=50, verbose_name=u'Otros Nombres')
	apellido_paterno = models.CharField(max_length=20, verbose_name=u'Apellido Paterno')
	apellido_materno = models.CharField(max_length=20, verbose_name=u'Apellido Materno')
	direccion_uno = models.TextField(max_length=100, verbose_name=u'Direccion Principal')
	direccion_dos = models.TextField(max_length=100, verbose_name=u'Direccion Secundaria')
	distrito = models.CharField(max_length=50, verbose_name=u'Distrito')
	ciudad = models.CharField(max_length=50, verbose_name=u'Ciudad')
	departamento = models.CharField(max_length=50, verbose_name=u'Departamento')
	telf_casa = models.CharField(max_length=10, verbose_name=u'Telefono Casa')
	telf_trabajo = models.CharField(max_length=10, verbose_name=u'Telefono Trabajo')
	telf_movil = models.CharField(max_length=10, verbose_name=u'Celular')
	mail_personal = models.EmailField(max_length=75, verbose_name=u'Correo Personal')
	mail_trabajo = models.EmailField(max_length=75, verbose_name=u'Correo Laboral')
	fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, verbose_name=u'Fecha de Nacimiento')
	fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False, verbose_name=u'Fecha de Ingreso')
	rol = models.ForeignKey('Rol')
	genero = models.ForeignKey('Genero')
	foto = models.ImageField(upload_to='foto_persona', blank=True)

	def __unicode__(self):
		return self.dni

