
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre de la Categoria", blank=False, null=False,max_length=100)
    estado = models.BooleanField('Categoria Activada/Desactivada', default=True)
    fecha_creacion = models.DateField("Fecha de Creacion",auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres del autor',max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos del autor',max_length=100, blank=False, null=False)
    nacionalidad = models.CharField('Nacionalidad del autor',max_length=100, blank=False)
    facebook = models.CharField("Facebook del autor", blank=True, null=True,max_length=100)
    Instagram = models.CharField("Instagram del autor", blank=True, null=True, max_length=100)
    twitter = models.CharField("Twitter del autor", blank=True,null=True,max_length=100)
    web = models.URLField("Web del autor", blank=True, null=True)
    email = models.EmailField("Email del autor", blank=False, null=False)
    estado = models.BooleanField("Autor activo/no Activo",default=True)
    fecha_creacion = models.DateTimeField("Fecha de Cracion", auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        db_table = 'Autor'

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=100,blank=False, null=False)
    slug = models.CharField('slug',max_length=100, blank=False,null=False)
    descripcion = models.CharField('Descripcion',max_length=100, blank=False, null=False)
    contenido = RichTextField(null=False)
    imagen = models.URLField('Imagen',max_length=300, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE, related_name='post')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, related_name='categoria')
    estado = models.BooleanField("Publicado/No Publicado", default=True)
    fecha_creacion = models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'Post'

    def __str__(self):
        return "{0}.{1}".format(self.descripcion, self.categoria)
