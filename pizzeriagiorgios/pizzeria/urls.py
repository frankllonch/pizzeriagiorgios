from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import PizzaViewSet, IngredienteViewSet

# Configuración de las rutas de la API RESTful
router = DefaultRouter()
router.register('pizzas', PizzaViewSet)
router.register('ingredientes', IngredienteViewSet)

# Rutas adicionales para las vistas del proyecto
urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('agregar-ingrediente/', views.agregar_ingrediente, name='agregar_ingrediente'),
    path('cart/', views.cart, name='cart'),
    path('order-status/', views.order_status, name='order_status'),
]

# Agrega las rutas de la API RESTful al conjunto de URLs
urlpatterns += router.urls
