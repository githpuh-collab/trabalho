from django.test import TestCase
from django.urls import reverse

from .models import Cliente, Empresa, Produto


class LojaViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.empresa = Empresa.objects.create(nome='Petshop Teste', ramo='Petshop')
        cls.produto = Produto.objects.create(
            empresa=cls.empresa,
            nome='Racao Premium 10kg',
            preco='85.50',
        )

    def test_index_redirects_to_first_company(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(
            response,
            reverse('url_da_loja', kwargs={'empresa_id': self.empresa.id}),
        )

    def test_dashboard_displays_company_and_products(self):
        response = self.client.get(
            reverse('url_da_loja', kwargs={'empresa_id': self.empresa.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loja.html')
        self.assertContains(response, 'Lista de Produtos')
        self.assertContains(response, self.empresa.nome)
        self.assertContains(response, self.empresa.ramo)
        self.assertContains(response, self.produto.nome)
        self.assertNotContains(response, 'Clientes')

    def test_novo_cliente_get_renders_form(self):
        response = self.client.get(
            reverse('novo_cliente', kwargs={'empresa_id': self.empresa.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form_template.html')
        self.assertContains(response, 'Novo Cliente')
        self.assertContains(response, 'card p-4 shadow-sm')
        self.assertContains(response, 'btn btn-success')

    def test_novo_cliente_post_creates_client_for_company(self):
        response = self.client.post(
            reverse('novo_cliente', kwargs={'empresa_id': self.empresa.id}),
            {
                'nome': 'Joao Silva',
                'cpf': '123.456.789-00',
                'email': 'joao@example.com',
                'telefone': '(37) 99999-9999',
                'data_nascimento': '1990-01-01',
                'endereco': 'Rua A, 123',
                'cidade': 'Nova Porteirinha',
                'cep': '39530-000',
            },
        )

        self.assertRedirects(
            response,
            reverse('url_da_loja', kwargs={'empresa_id': self.empresa.id}),
        )
        self.assertEqual(Cliente.objects.count(), 1)
        cliente = Cliente.objects.get()
        self.assertEqual(cliente.empresa, self.empresa)
        self.assertEqual(cliente.nome, 'Joao Silva')

    def test_novo_cliente_post_invalid_does_not_create_client(self):
        response = self.client.post(
            reverse('novo_cliente', kwargs={'empresa_id': self.empresa.id}),
            {
                'nome': '',
                'cpf': '',
                'email': 'email-invalido',
                'telefone': '',
                'data_nascimento': '',
                'endereco': '',
                'cidade': '',
                'cep': '',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Cliente.objects.count(), 0)
        self.assertTrue(response.context['form'].errors)

    def test_novo_produto_get_renders_form(self):
        response = self.client.get(
            reverse('novo_produto', kwargs={'empresa_id': self.empresa.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form_template.html')
        self.assertContains(response, 'Novo Produto')
        self.assertContains(response, 'card p-4 shadow-sm')
        self.assertContains(response, 'btn btn-success')

    def test_novo_produto_post_creates_product_for_company(self):
        response = self.client.post(
            reverse('novo_produto', kwargs={'empresa_id': self.empresa.id}),
            {'nome': 'Coleira Azul', 'preco': '29.90'},
        )

        self.assertRedirects(
            response,
            reverse('url_da_loja', kwargs={'empresa_id': self.empresa.id}),
        )
        self.assertEqual(Produto.objects.count(), 2)
        produto = Produto.objects.get(nome='Coleira Azul')
        self.assertEqual(produto.empresa, self.empresa)

    def test_novo_produto_post_invalid_does_not_create_product(self):
        response = self.client.post(
            reverse('novo_produto', kwargs={'empresa_id': self.empresa.id}),
            {'nome': '', 'preco': ''},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Produto.objects.count(), 1)
        self.assertTrue(response.context['form'].errors)

    def test_dashboard_returns_404_for_missing_company(self):
        response = self.client.get(reverse('url_da_loja', kwargs={'empresa_id': 999}))
        self.assertEqual(response.status_code, 404)
