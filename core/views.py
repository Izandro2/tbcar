from django.shortcuts import render, redirect
from core.forms import FormCliente, FormVeiculo, FormTabela, FormRotativo, FormMensalista, FormMarca
from core.models import Cliente, Marca, Veiculo, Tabela, Rotativo, Mensalista
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'


def home(request):
    return render(request, 'core/index.html')

@login_required()
def altera_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_clientes')
        contexto = {'form': form, 'txt_titulo': 'EditCliente', 'txt_descricao': 'Altera Cliente'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')

@login_required()
def altera_veiculo(request, id):
    if request.user.is_staff:
        obj2 = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj2)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_veiculos')
        contexto = {'form': form, 'txt_titulo': 'EditCliente', 'txt_descricao': 'Altera Veiculo'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')


@login_required()
def cadastro_cliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form':form, 'txt_titulo':'cad_cliente', 'txt_descricao':'Cadastro de Cliente'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required()
def listagem_clientes(request):
    if request.POST and request.POST["pesquisa_input"]:
        dados = Cliente.objects.filter(nome__icontains=request.POST["pesquisa_input"])
    else:
        dados = Cliente.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_clientes.html', contexto)

@login_required()
def cadastro_veiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form':form, 'txt_titulo':'cad_veic', 'txt_descricao':'Cadastro de Veiculo'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required()
def listagem_veiculos(request):

    if request.POST and request.POST["pesquisa_input"]:
        dados = Veiculo.objects.filter(placa__icontains=request.POST["pesquisa_input"]  )
    else:
        dados = Veiculo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_veiculos.html', contexto)



@login_required()
def cadastro_tabela(request):
    if request.user.is_staff:
        form = FormTabela(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form':form, 'txt_titulo':'cad_tab', 'txt_descricao':'Cadastro de Tabelas'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required()
def listagem_tabelas(request):






    if request.user.is_staff:

        if request.POST and request.POST["pesquisa_input"]:
            dados = Tabela.objects.filter(descricao__icontains=request.POST["pesquisa_input"])
        else:
            dados = Tabela.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_tabelas.html', contexto)

    return render(request, 'aviso.html')


@login_required()
def altera_tabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id=id)
        form = FormTabela(request.POST or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_tabelas')
        contexto = {'form': form, 'txt_titulo': 'EditTabela', 'txt_descricao': 'Altera Tabela'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')

@login_required()
def exclui_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    contexto={'txt_tipo':obj.nome, 'txt_url': '/listagem_clientes/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo':'Cliente'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)

@login_required()
def exclui_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    contexto={'txt_tipo':obj.modelo, 'txt_url': '/listagem_veiculos/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo':'Veiculo'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)

@login_required()
def cadastro_rotativo(request):
    if request.user.is_staff:
        form = FormRotativo(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form':form, 'txt_titulo':'cad_rot', 'txt_descricao':'Cadastro Rotativo'}
        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)
    return render(request, 'aviso.html')

@login_required()
def listagem_rotativos(request):



    if request.user.is_staff:

        if request.POST and request.POST["pesquisa_input"]:
            dados = Rotativo.objects.filter(entrada__startswith=request.POST["pesquisa_input"])
        else:
            dados = Rotativo.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_rotativos.html', contexto)

    return render(request, 'aviso.html')

@login_required()
def cadastro_mensalista(request):
    if request.user.is_staff:
        form = FormMensalista(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form':form, 'txt_titulo':'cad_mens', 'txt_descricao':'Cadastro Mensalista'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required()
def listagem_mensalistas(request):
    if request.user.is_staff:
        dados = Mensalista.objects.all()
        contexto = {'dados':dados}
        return render(request, 'core/listagem_mensalistas.html', contexto)
    return render(request, 'aviso.html')

@login_required()
def exclui_rotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    contexto={'txt_tipo':obj.id_veiculo, 'txt_url': '/listagem_rotativos/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo':'Rotativo'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)

@login_required()
def exclui_mensalista(request, id):
    obj = Mensalista.objects.get(id=id)
    contexto={'txt_tipo':obj.id_veiculo, 'txt_url': '/listagem_mensalistas/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo':'Mensalista'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)

@login_required()
def altera_rotativo(request, id):
        obj = Rotativo.objects.get(id=id)
        form = FormRotativo(request.POST or None, instance=obj)
        if form.is_valid():
            obj.calcula_total()
            form.save()
            return redirect('url_listagem_rotativos')
        else:
            contexto = {'form': form, 'txt_titulo': 'AltRot', 'txt_descricao': 'Altera Rotativo'}
        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)

@login_required()
def altera_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_mensalistas')
        contexto = {'form': form, 'txt_titulo': 'EditMensalista', 'txt_descricao': 'Altera Mensalista'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')

@login_required()
def cadastro_marca(request):
    if request.user.is_staff:
        form = FormMarca(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form':form, 'txt_titulo':'cad_marca', 'txt_descricao':'Cadastro Marca'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required()
def altera_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id=id)
        form = FormMarca(request.POST or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_marca')
        contexto = {'form': form, 'txt_titulo': 'Edit_marca', 'txt_descricao': 'Altera Marca'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')

@login_required()
def exclui_marca(request, id):
    obj = Marca.objects.get(id=id)
    contexto={'txt_tipo':obj.id, 'txt_url': '/listagem_marcas/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo':'Marc'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)

@login_required()
def listagem_marcas(request):
    if request.user.is_staff:
        dados = Marca.objects.all()
        contexto = {'dados':dados}
        return render(request, 'core/listagem_marcas.html', contexto)
    return render(request, 'aviso.html')
