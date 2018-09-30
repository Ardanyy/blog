from django.db import models

# Create your models here.
class Post(models.Model):
        titulo = models.CharField(max_length=200, verbose_name="Titulo")
        sub = models.TextField(verbose_name="Sub Titulo")
        description = models.TextField(verbose_name="Descripcion")
        created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
        updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

        class Meta:
                verbose_name="Proyecto" 
                verbose_name_plural="proyectos"
                ordering = ["-created"]

        def __str__(self): #devuelve el nombre del proyecto
                return self.titulo