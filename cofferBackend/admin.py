from django.contrib import admin
from .models import Usuario, Carteira, Categoria, Lancamento

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Carteira)
admin.site.register(Categoria)
admin.site.register(Lancamento)