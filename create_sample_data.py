"""
Cria dados de exemplo: uma Empresa e alguns Produtos.
Executar na raiz do projeto (onde está manage.py):
    python create_sample_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from core_loja.models import Empresa, Produto

empresa, created = Empresa.objects.get_or_create(nome='Loja Exemplo', ramo='Mercearia')
if created:
    print(f'Empresa criada: {empresa.nome} (id={empresa.id})')
else:
    print(f'Empresa existente: {empresa.nome} (id={empresa.id})')

produtos = [
    ('Arroz 1kg', '12.50'),
    ('Feijão 1kg', '8.30'),
    ('Açúcar 1kg', '4.20'),
]

for nome, preco in produtos:
    p, created = Produto.objects.get_or_create(empresa=empresa, nome=nome, defaults={'preco': preco})
    if created:
        print(f'Produto criado: {p.nome} - R$ {p.preco}')
    else:
        print(f'Produto existente: {p.nome} - R$ {p.preco}')

print('Dados de exemplo prontos.')
