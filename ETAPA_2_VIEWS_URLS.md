# Views e URLs

`core/urls.py` e a fonte de verdade das rotas publicas do projeto.

## Rotas

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('loja/<int:empresa_id>/', views.dashboard_loja, name='url_da_loja'),
    path(
        'loja/<int:empresa_id>/novo-cliente/',
        views.cadastrar_item,
        {'tipo': 'cliente'},
        name='novo_cliente',
    ),
    path(
        'loja/<int:empresa_id>/novo-produto/',
        views.cadastrar_item,
        {'tipo': 'produto'},
        name='novo_produto',
    ),
]
```

## Views

### `index`

- busca a primeira empresa cadastrada
- redireciona para o dashboard dessa empresa
- se nao houver empresa, redireciona para `/admin/`

### `dashboard_loja`

- recebe `empresa_id`
- busca a `Empresa` com `get_object_or_404`
- lista `Produto.objects.filter(empresa=empresa)`
- renderiza `loja.html` com `empresa` e `produtos`

### `cadastrar_item`

- recebe `empresa_id` e `tipo`
- usa `ClienteForm` quando `tipo == 'cliente'`
- usa `ProdutoForm` quando `tipo == 'produto'`
- salva com `form.save(commit=False)`
- define `item.empresa = empresa`
- redireciona para `url_da_loja` apos sucesso

## Fluxo esperado

1. O usuario entra em `/loja/1/`.
2. O dashboard mostra a empresa e os produtos dessa empresa.
3. O usuario abre `/loja/1/novo-cliente/` ou `/loja/1/novo-produto/`.
4. O formulario salva o registro ja vinculado a empresa da URL.
