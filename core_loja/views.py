from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClienteForm, ProdutoForm
from .models import Empresa, Produto


def dashboard_loja(request, empresa_id):
    """Tela que lista os produtos de uma empresa."""
    empresa = get_object_or_404(Empresa, id=empresa_id)
    produtos = Produto.objects.filter(empresa=empresa)
    return render(request, 'loja.html', {'empresa': empresa, 'produtos': produtos})


def cadastrar_item(request, empresa_id, tipo):
    """Tela de cadastro generica para Cliente e Produto."""
    empresa = get_object_or_404(Empresa, id=empresa_id)

    if tipo == 'cliente':
        form = ClienteForm(request.POST or None)
        titulo = 'Novo Cliente'
    elif tipo == 'produto':
        form = ProdutoForm(request.POST or None)
        titulo = 'Novo Produto'
    else:
        raise Http404('Tipo de cadastro invalido.')

    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.empresa = empresa
        item.save()
        return redirect('url_da_loja', empresa_id=empresa.id)

    return render(
        request,
        'form_template.html',
        {'form': form, 'empresa': empresa, 'titulo': titulo},
    )


def index(request):
    """Redireciona a raiz para a primeira empresa cadastrada ou para o admin."""
    empresa = Empresa.objects.first()
    if empresa:
        return redirect('url_da_loja', empresa_id=empresa.id)
    return redirect('/admin/')
