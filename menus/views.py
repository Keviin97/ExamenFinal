from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import MenuForm
from .models import Menu, Venta, Plato


def menu_nuevo(request):
    if request.method == "POST":
        formulario = MenuForm(request.POST)
        if formulario.is_valid():
            menu = Menu.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'], total = formulario.cleaned_data['total'])
            for plato_id in request.POST.getlist('platillos'):
                venta = Venta(plato_id=plato_id, menu_id = menu.id)
                venta.save()
            messages.add_message(request, messages.SUCCESS, 'Menu Guardado Exitosamente')
    else:
        formulario = MenuForm()
    return render(request, 'menus/menu_editar.html', {'formulario': formulario})

def post_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menus/post_detail.html', {'menu': menu})