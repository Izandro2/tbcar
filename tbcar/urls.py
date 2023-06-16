"""tbcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import home, cadastro_cliente, listagem_clientes, cadastro_veiculo, listagem_veiculos, cadastro_tabela, \
    listagem_tabelas, Registrar, altera_cliente, altera_veiculo, altera_tabela, exclui_cliente, exclui_veiculo, \
    listagem_rotativos, listagem_mensalistas, cadastro_mensalista, cadastro_rotativo, altera_rotativo, \
    altera_mensalista, exclui_mensalista, exclui_rotativo, cadastro_marca, altera_marca, exclui_marca, listagem_marcas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('captcha/', include('captcha.urls')),
    path('', home , name='url_principal'),
    path('cadastro_cliente/',cadastro_cliente, name='url_cadastro_cliente'),
    path('listagem_clientes/',listagem_clientes, name='url_listagem_clientes'),
    path('cadastro_veiculo/',cadastro_veiculo, name='url_cadastro_veiculo'),
    path('listagem_veiculos/',listagem_veiculos, name='url_listagem_veiculos'),
    path('cadastro_tabela/',cadastro_tabela, name='url_cadastro_tabela'),
    path('listagem_tabelas/', listagem_tabelas, name='url_listagem_tabelas'),
    path('altera_cliente/<int:id>/', altera_cliente, name='url_altera_cliente'),
    path('altera_veiculo/<int:id>/', altera_veiculo, name='url_altera_veiculo'),
    path('altera_tabela/<int:id>/', altera_tabela, name='url_altera_tabela'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculo'),
    path('listagem_rotativos/', listagem_rotativos, name='url_listagem_rotativos'),
    path('listagem_mensalistas/', listagem_mensalistas, name='url_listagem_mensalistas'),
    path('cadastro_mensalista/',cadastro_mensalista, name='url_cadastro_mensalista'),
    path('cadastro_rotativo/',cadastro_rotativo, name='url_cadastro_rotativo'),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),
    path('exclui_mensalista/<int:id>/', exclui_mensalista, name='url_exclui_mensalista'),
    path('altera_mensalista/<int:id>/', altera_mensalista, name='url_altera_mensalista'),
    path('altera_rotativo/<int:id>/', altera_rotativo, name='url_altera_rotativo'),
    path('cadastro_marca/',cadastro_marca, name='url_cadastro_marca'),
    path('altera_marca/<int:id>/', altera_marca, name='url_altera_marca'),
    path('exclui_marca/<int:id>/', exclui_marca, name='url_exclui_marca'),
    path('listagem_marcas/', listagem_marcas, name='url_listagem_marcas')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)