from django.contrib import admin
from menus.models import Plato, PlatoAdmin, Menu, MenuAdmin

admin.site.register(Plato, PlatoAdmin)
admin.site.register(Menu, MenuAdmin)
