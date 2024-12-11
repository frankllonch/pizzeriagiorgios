from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    calorias = models.FloatField()
    grasas = models.FloatField()
    proteinas = models.FloatField()
    carbohidratos = models.FloatField()

    def __str__(self):
        return self.nombre

class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    ingredientes = models.ManyToManyField(Ingrediente)
    tamanos = models.CharField(
        max_length=10,
        choices=[('pequeño', 'Pequeño'), ('mediano', 'Mediano'), ('grande', 'Grande')],
    )

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)
    estado = models.CharField(
        max_length=15,
        choices=[
            ('preparando', 'Preparando'),
            ('en camino', 'En Camino'),
            ('entregado', 'Entregado'),
        ],
    )
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
