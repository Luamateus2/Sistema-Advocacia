# Sistema de Gestão para Escritório de Advocacia Previdenciária

## Descrição
Este projeto foi desenvolvido como parte da conclusão de uma disciplina do curso de Sistemas de Informação e tem como objetivo simular o funcionamento de um sistema de gestão de clientes e processos para um escritório de advocacia previdenciária. 

O sistema permite:
- O cadastro de clientes
- A simulação do cadastro de processos jurídicos relacionados à previdência
- A listagem de clientes
- A alteração de seus dados

## Funcionalidades
O sistema oferece as seguintes funcionalidades:

- **Cadastro de Clientes**: Inserção de informações pessoais de clientes como nome, CPF e dados relacionados à previdência.
- **Listagem de Clientes**: Exibição de todos os clientes cadastrados no sistema.
- **Alteração de Dados**: Permite a edição das informações dos clientes existentes.
- **Simulação de Cadastro de Processos**: Simulação do cadastro de processos jurídicos vinculados a clientes.
- **Controle de Acesso**: Apenas as páginas de cadastro e login possuem acesso livre, garantindo maior segurança ao sistema.

## Tecnologias Utilizadas

### Back-end:
- Django (Python)

### Banco de Dados:
- SQLite (ambiente de desenvolvimento)

### Front-end:
- HTML5
- CSS3
- Django
- Bootstrap 5

## Estrutura do Projeto
```
/
|-- templates/                # Templates HTML do projeto
|-- advocacia/   # Diretório raiz do projeto Django
|-- task/            # Aplicativo responsável pela gestão de tarefas/processos
|-- requirements.txt          # Arquivo com as dependências do projeto
```

## Como Executar o Projeto
### 1. Clonar o Repositório
```sh
git clone https://github.com/Luamateus2/Sistema-Advocacia.git
cd sistema-advocacia
```

### 2. Criar e Ativar o Ambiente Virtual
```sh
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### 3. Instalar as Dependências
```sh
pip install -r requirements.txt
```

### 4. Aplicar as Migrações do Banco de Dados
```sh
python manage.py migrate
```

### 5. Criar um Superusuário (Opcional, para acesso ao admin)
```sh
python manage.py createsuperuser
```

### 6. Executar o Servidor
```sh
python manage.py runserver
```

Acesse o sistema no navegador pelo endereço: `http://127.0.0.1:8000/`

## Licença
Este projeto foi desenvolvido para fins acadêmicos e não possui fins comerciais.

---

**Autor:** Luana Karoline
**Contato:** luanakarolineliramateus2021@gmail.com

