from django.db import models


# Create your models here.

class VehiculoModel(models.Model):
    MARCA_OPTIONS = (
        ('Fiat', 'Fiat'), 
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )

    CATEGORIAS_OPTIONS = (
        ('Particular', 'Particular'), 
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    marca = models.CharField(max_length= 20, choices = MARCA_OPTIONS, default = 'Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices = CATEGORIAS_OPTIONS, default = 'Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

#Este es el permiso aaaaaaaa ya entendi, lento pero seguro jajaja
    class Meta:
        permissions = (
            ("visualizar_catalogo", "Puede visualizar_catalogo"),
        
        ) 
        verbose_name_plural =  "Usuario registrado"

    def __str__(self):
        return self.marca







    