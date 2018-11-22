from django.db import models
from django.contrib import admin

class Plato(models.Model):
    nombre  =   models.CharField(max_length=200)
    precio  =   models.IntegerField()

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

class VentaInLine(admin.TabularInline):
    model = Venta
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)

class MenuAdmin (admin.ModelAdmin):
    inlines = (VentaInLine,)