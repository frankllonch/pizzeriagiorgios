from django.shortcuts import render
from .models import Pizza

# Create your views here.

def menu(request):
    pizzas = Pizza.objects.all()
    return render(request, 'menu.html', {'pizzas': pizzas})



from django.shortcuts import render, redirect
from .models import Ingrediente
from .utils import obtener_info_nutricional

def agregar_ingrediente(request):
    """
    Vista para agregar un ingrediente con información nutricional.
    """
    if request.method == 'POST':
        nombre = request.POST['nombre']
        try:
            datos = obtener_info_nutricional(nombre)
            Ingrediente.objects.create(
                nombre=nombre,
                calorias=datos.get('calories', 0),
                grasas=datos['totalNutrients'].get('FAT', {}).get('quantity', 0),
                proteinas=datos['totalNutrients'].get('PROCNT', {}).get('quantity', 0),
                carbohidratos=datos['totalNutrients'].get('CHOCDF', {}).get('quantity', 0),
            )
            return redirect('menu')  # Redirige al menú después de agregar
        except Exception as e:
            return render(request, 'error.html', {'mensaje': str(e)})
    return render(request, 'agregar_ingrediente.html')


from rest_framework.viewsets import ModelViewSet
from .models import Pizza, Ingrediente
from .serializers import PizzaSerializer, IngredienteSerializer

class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class IngredienteViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer


from django.shortcuts import render
from .models import Pedido

def cart(request):
    """
    Vista para mostrar el carrito de compras.
    """
    # Ejemplo de datos simulados, puedes conectar esto con la lógica del modelo.
    cart_items = [
        {"pizza": {"nombre": "Margherita"}, "cantidad": 2, "total": 15.99},
        {"pizza": {"nombre": "Pepperoni"}, "cantidad": 1, "total": 12.50},
    ]
    total = sum(item['total'] for item in cart_items)
    return render(request, 'pizzeria/cart.html', {'cart': cart_items, 'total': total})

def order_status(request):
    """
    Vista para mostrar el estado del pedido.
    """
    # Datos simulados, conecta esto con tu modelo `Pedido`
    pedido = {
        "estado": "Preparando",
        "fecha": "2024-12-11",
        "pizzas": [{"nombre": "Margherita", "tamanos": "Mediano"}],
    }
    return render(request, 'pizzeria/order_status.html', pedido)
