# 🛒 Cadastro de Produtos

Aplicação web simples para cadastrar produtos e calcular o total de um carrinho de compras, desenvolvida com **Flask** e **Bootstrap 5**.

## Sobre o projeto

O usuário informa o nome e o preço de cada produto em um formulário. Os itens aparecem em uma tabela e o total do carrinho é recalculado automaticamente a cada novo cadastro.

##  Funcionalidades

- Cadastro de produtos com nome e preço
- Listagem dos itens em uma tabela responsiva
- Cálculo automático do total do carrinho
- Mensagem amigável quando não há produtos cadastrados
- Valores formatados em reais (R$) com duas casas decimais

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Jinja2](https://jinja.palletsprojects.com/) (templates)
- [Bootstrap 5](https://getbootstrap.com/) (via CDN)

##  Estrutura do projeto

```
cadastro-produtos/
├── app.py              # Rotas e lógica da aplicação
└── templates/
    └── index.html      # Interface (formulário + tabela)
```

> **Importante:** o Flask exige que o `index.html` fique dentro de uma pasta chamada `templates`.

##  Como executar

### Pré-requisitos

- Python 3.8 ou superior
- pip

### Passo a passo

1. **Clone ou baixe** o projeto e acesse a pasta:

   ```bash
   cd cadastro-produtos
   ```

2. **(Opcional) Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/macOS
   source venv/bin/activate
   ```

3. **Instale o Flask:**

   ```bash
   pip install flask
   ```

4. **Execute a aplicação:**

   ```bash
   python app.py
   ```

5. **Acesse no navegador:**

   ```
   http://127.0.0.1:5000
   ```

## ⚙️ Como funciona

A rota `/` aceita dois métodos:

- `GET`: exibe a página com o formulário e a lista de produtos.
- `POST`: recebe nome e preço, salva o produto em uma lista em memória e recarrega a página.

Antes de renderizar o template, o total é calculado somando o preço de todos os itens da lista.

##  Limitações

- Os dados ficam apenas em memória: ao reiniciar o servidor, a lista é perdida
- Não é possível editar ou remover produtos
- Não há persistência em banco de dados

##  Possíveis melhorias

- [ ] Salvar os produtos em um banco de dados (SQLite)
- [ ] Adicionar botões para editar e excluir itens
- [ ] Incluir campo de quantidade por produto
- [ ] Validar valores negativos no preço
- [ ] Adicionar botão para limpar o carrinho

##  Licença

Este projeto foi desenvolvido para fins de estudo e pode ser usado livremente.
