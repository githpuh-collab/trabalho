from django.db import models

# 1. A Empresa
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    ramo = models.CharField(max_length=50)
    # Ex: Farmácia, Petshop, Mercado
    def __str__(self):
        return self.nome

# 2. Produto
class Produto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.nome} - ({self.empresa.nome})"

# 3. Cliente
class Cliente(models.Model):  # Use sempre no singular por boa prática
    # 1. Conexão SaaS (Obrigatório: de qual empresa é este cliente?)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    # 2. Dados Pessoais
    nome = models.CharField(max_length=150)  # Texto curto com limite
    cpf = models.CharField(max_length=14, unique=True)  # Unique impede CPF duplicado
    email = models.EmailField()  # Valida automaticamente se tem @ e .com
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()  # Abre um calendário no Admin
    # 3. Endereço
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100, default="Nova Porteirinha")
    cep = models.CharField(max_length=9)
    # 4. Controle Interno
    data_cadastro = models.DateTimeField(auto_now_add=True)  # Grava a data/hora sozinho ao criar
    ativo = models.BooleanField(default=True)  # Para "bloquear" clientes sem excluir os dados
    def __str__(self):
        return self.nome
