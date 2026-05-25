# Trabalho-main

Projeto Django alinhado ao escopo dos arquivos `codigo_backend.pdf` e
`codigo_frontend.pdf`.

## O que esta concluido

- Modelos `Empresa`, `Produto` e `Cliente`
- Admin Django para os tres modelos
- Formularios `ClienteForm` e `ProdutoForm`
- Templates `base.html`, `form_template.html` e `loja.html`
- Views `index`, `dashboard_loja` e `cadastrar_item`
- Rotas publicas:
  - `/`
  - `/admin/`
  - `/loja/<empresa_id>/`
  - `/loja/<empresa_id>/novo-cliente/`
  - `/loja/<empresa_id>/novo-produto/`
- Testes automatizados para o fluxo principal

## Como executar

Abra um terminal na pasta que contem `manage.py`, que neste projeto e
`Trabalho-main/Trabalho-main`.

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python create_superuser.py
python create_sample_data.py
python manage.py runserver
```

Se preferir criar o usuario manualmente, use `python manage.py createsuperuser`.

## Validacao automatica

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

## Arquivos de apoio

- `SETUP.md`: instalacao e execucao
- `TESTE_RAPIDO.txt`: roteiro curto de verificacao manual
- `GUIA_TESTE_ETAPA2.md`: guia detalhado de testes
- `URLS_REFERENCIA.txt`: resumo das rotas publicas
- `ETAPA_2_VIEWS_URLS.md`: explicacao tecnica das views e URLs

## Escopo da entrega

Este repositorio esta concluido dentro do escopo dos dois PDFs.
Funcionalidades como autenticacao, permissao, edicao e exclusao nao fazem
parte desta entrega.
