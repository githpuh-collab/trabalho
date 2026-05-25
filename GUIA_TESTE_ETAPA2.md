# Guia de Teste

Este guia valida a entrega final dentro do escopo dos PDFs.

## Preparacao

```bash
python manage.py migrate
python create_superuser.py
python create_sample_data.py
python manage.py runserver
```

Tambem e valido criar a empresa manualmente pelo admin em vez de usar
`create_sample_data.py`.

## Teste 1: Dashboard

URL: `http://localhost:8000/loja/1/`

Esperado:

- pagina renderiza sem erro
- sidebar mostra nome e ramo da empresa
- titulo `Lista de Produtos`
- tabela lista apenas produtos da empresa

## Teste 2: Novo Cliente - GET

URL: `http://localhost:8000/loja/1/novo-cliente/`

Esperado:

- titulo `Novo Cliente`
- campos do `ClienteForm`
- formulario com `card p-4 shadow-sm`
- botao `Salvar` com classe `btn btn-success`

## Teste 3: Novo Cliente - POST valido

URL: `http://localhost:8000/loja/1/novo-cliente/`

Dados:

- Nome: `Joao Silva`
- CPF: `123.456.789-00`
- Email: `joao@email.com`
- Telefone: `(37) 99999-9999`
- Data Nascimento: `1990-01-01`
- Endereco: `Rua A, 123`
- Cidade: `Nova Porteirinha`
- CEP: `39530-000`

Esperado:

- redirect para `/loja/1/`
- cliente salvo com a empresa da URL

## Teste 4: Novo Cliente - POST invalido

Envie o formulario vazio ou com email invalido.

Esperado:

- resposta continua na mesma pagina
- formulario volta com erros
- nenhum cliente novo e salvo

## Teste 5: Novo Produto - GET

URL: `http://localhost:8000/loja/1/novo-produto/`

Esperado:

- titulo `Novo Produto`
- formulario com campos `nome` e `preco`
- card Bootstrap com botao verde

## Teste 6: Novo Produto - POST valido

URL: `http://localhost:8000/loja/1/novo-produto/`

Dados:

- Nome: `Coleira Azul`
- Preco: `29.90`

Esperado:

- redirect para `/loja/1/`
- produto aparece na tabela do dashboard
- produto fica vinculado a empresa da URL

## Teste 7: Novo Produto - POST invalido

Envie o formulario vazio.

Esperado:

- resposta continua na mesma pagina
- formulario volta com erros
- nenhum produto novo e salvo

## Teste 8: Empresa inexistente

URL: `http://localhost:8000/loja/999/`

Esperado:

- retorno `404 Not Found`

## Teste automatizado

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```
