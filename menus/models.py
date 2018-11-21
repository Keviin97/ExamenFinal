from django.db import models
from django.contrib import admin

class Plato(models.Model):
    nombre  =   models.CharField(max_length=200)
    precio  =   models.IntegerField()

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre  =   models.CharField(max_length=200)
    apellidos  =   models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    puesto = models.CharField(max_length=200)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre  =   models.CharField(max_length=200)
    apellidos  =   models.CharField(max_length=200)
    nit = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre    = models.CharField(max_length=200)
    descripcion      = models.CharField(max_length=200)
    total = models.IntegerField()
    platillos   = models.ManyToManyField(Plato, through='Venta')

    def __str__(self):
        return self.nombre

class Venta (models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class VentaInLine(admin.TabularInline):
    model = Venta
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)

class MenuAdmin (admin.ModelAdmin):
    inlines = (VentaInLine,)

class ClienteAdmin (admin.ModelAdmin):
    inlines = (VentaInLine,)
class EmpleadoAdmin (admin.ModelAdmin):
    inlines = (VentaInLine,)