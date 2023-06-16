from django.contrib import admin
from core.models import Cliente, Veiculo, Marca, Tabela, Rotativo, Mensalista

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Marca)
admin.site.register(Tabela)
admin.site.register(Rotativo)
admin.site.register(Mensalista)