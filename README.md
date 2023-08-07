## Sobre

O Library é um projeto Back-end, desenvolvido utilizando as tecnologias:
- Python + Django
- PostgreSQL

## Descrição
Uma aplicação que faz a gestão de uma biblioteca.

## Iniciar o projeto
1. Realize o clone o repositório.
2. Digite no terminal o comando python -m venv venv para criar o seu ambiente virtual (Git Bash)
3. Para executar o ambiente virtual no windows usando o GitBash digite :  source venv/Scripts/activate
4. Faça a instalação das dependências do projeto, digitando: pip install -r requirements.txt.
5. Deve-se criar o arquivo .env e seguir o modelo do arquivo .env.example para fazer a conexão com o banco de dados.
6. Será necessário realizar as migrações (generate e run) para que sejam criadas as tabelas no seu banco de dados.
Digite no terminal do VsCode:
6.1. Para criar a migração: python manage.py makemigrations
6.2. Para executar a migration e criar no Banco de Dados: python manage.py migrate
7. Caso deseje, você pode verificar no DBeaver (ou similar) ou no psql se as tabelas foram criadas.
8. Para rodar o projeto, digite: python manage.py runserver

## EndPoints do projeto

|N| Método HTTP | Endpoint             | Autenticação            | Descrição da Rota                                 |
|- | -----------| -------------------- | ----------------------- | ------------------------------------------------  |
|1 | POST       | /login/              | Rota livre (sem Token)  | Faz o login e gera o Token do usuário             |
|2 | POST       | /users/              | Rota livre (sem Token)  | Criação de usuário                                |
|3 | GET        | /users/              | Rota livre (sem Token)  | Lista todos os usuários                           |
|4 | GET        | /users/:id/          | Token obrigatório       | Lista o usuário com id requisitado                |
|5 | PATCH      | /users/:id/          | Token obrigatório       | Atualiza os dados do usuário                      |
|6 | DELETE     | /users/:id/          | Token obrigatório       | Deleta o usuário                                  |
|7 | POST       | /books/              | Token obrigatório       | Criação de cliente                                |
|8 | GET        | /books/              | Rota livre (sem Token)  | Lista todos os livros da biblioteca               |
|9 | GET        | /books/:id/          | Token obrigatório       | Lista o livro com id requisitado                  |
|10| PATCH      | /books/:id/          | Token obrigatório       | Atualiza os dados do cliente                      |
|11| PATCH      | /books/:id/follow/   | Token obrigatório       | Segue o livro, quando disponivel avisa por e-mail |
|12| DELETE     | /books/:id/unfollow/ | Token obrigatório       | Deixar de seguir o livro                          |
|13| POST       | /copy/:id/           | Token obrigatório       | Separa o livro para empréstimo                    |
|14| GET        | /copy/:id/           | Rota livre (sem Token)  | Lista os livros separados para empréstimo         |
|15| POST       | /loan/               | Rota livre (sem Token)  | Realiza o empréstimo do livro                     |
|16| GET        | /loan/               | Rota livre (sem Token)  | Lista os livros emprestados                       |
|17| PATCH      | /loan/:id/           | Rota livre (sem Token)  | Devolve o livro emprestado                        |


## Detalhes dos EndPoints

1. /login/ (POST)
Body: Text Format - JSON
Auth Types: No Authentication

Requisição: 
{
	"username": "Insira o usuário"
	"password": "Insira a senha" 
}

Resposta:
200 - Sucesso
{
	"token": "valor do Token"
}

##

2. /users/ (POST)
Body: Text Format - JSON
Auth Types: No Authentication

Requisição:
{
	"username": "Insira o usuário em string",
	"email": "Insira o e-mail, máximo de 50 caracteres e string",
	"password": "Insira sua senha em string",
	"full_name": "Insira o nome completo em string"
}

Resposta:
200 - Sucesso
	{
		"id": "Id gerado em uuid",
		"username": "Nome completo",
		"email": "email",
		"full_name": "Telefone",
		"is_employee": "Um booleano que indica se o usuário é funcionário da biblioteca",
        "is_admin": "Um booleano que indica se o usuário é administrador do sistema",
        "is_block": "Um booleano que indica se o usuário está bloqueado, impedindo empréstimos",
	}

Caso esteja faltando algum dado obrigatório,
400 - Bad Request
{
    "message": "Informação do que está pendente"
}

Caso o username cadastrado já exista,
409 - Conflit
{
	"message": "username already exists"
}

Caso o e-mail cadastrado já exista,
409 - Conflit
{
	"message": "email already exists"
}

##

3. /users/ (GET)
Body: No Body
Auth Types: No Authentication
Resposta: 
200 - Sucesso
[
	{
		"id": "Id gerado",
		"username": "Nome completo",
		"email": "email",
		"full_name": "Telefone",
		"is_employee": "Um booleano que indica se o usuário é funcionário da biblioteca",
        "is_admin": "Um booleano que indica se o usuário é administrador do sistema",
        "is_block": "Um booleano que indica se o usuário está bloqueado, impedindo empréstimos",
	},
	{
		"id": "Id gerado",
		"username": "Nome completo",
		"email": "email",
		"full_name": "Telefone",
		"is_employee": "Um booleano que indica se o usuário é funcionário da biblioteca",
        "is_admin": "Um booleano que indica se o usuário é administrador do sistema",
        "is_block": "Um booleano que indica se o usuário está bloqueado, impedindo empréstimos",
	},
]

## 

4. /users/:id/ (GET)
Body: No Body
Auth Types: Bearer Token
Resposta:
200 - Sucesso
	{
		"id": "Id gerado",
		"username": "Nome completo",
		"email": "email",
		"full_name": "Telefone",
		"is_employee": "Um booleano que indica se o usuário é funcionário da biblioteca",
        "is_admin": "Um booleano que indica se o usuário é administrador do sistema",
        "is_block": "Um booleano que indica se o usuário está bloqueado, impedindo empréstimos",
	}

Caso o id não seja encontrado
404 - Not Found
{
    "message": "user not found"
}

##

5. /users/:id/ (PATCH)
Body: Text Format - JSON
Auth Types: Bearer Token
Requisição:
{
    "campo(s)": "alteração"
}
Exemplo:
{
    "full_name": "Nome Completo"
}
Resposta:
200 - Sucesso
{
		"id": "Id gerado",
		"username": "Nome completo",
		"email": "email",
		"full_name": "Telefone",
		"is_employee": "Um booleano que indica se o usuário é funcionário da biblioteca",
        "is_admin": "Um booleano que indica se o usuário é administrador do sistema",
        "is_block": "Um booleano que indica se o usuário está bloqueado, impedindo empréstimos",
}

Caso esteja faltando algum dado obrigatório,
400 - Bad Request
{
    "message": "Informação do que está pendente"
}

Caso o id não seja encontrado
404 - Not Found
{
    "message": "user not found"
}

Caso o username cadastrado já exista,
409 - Conflit
{
	"message": "username already exists"
}

Caso o e-mail cadastrado já exista,
409 - Conflit
{
	"message": "email already exists"
}

## 

6. /users/ (DELETE)
Body: No Body
Auth Types: Bearer Token
Resposta:
Em caso de sucesso
204 - No Content

Caso o id não seja encontrado
404 - Not Found
{
    "message": "user not found"
}

##

7. /books/ (POST)
Body: Text Format - JSON
Auth Types: Bearer Token
Requisição:
{
	"name": "Nome do Livro",
	"author": "Autor do Livro",
	"description": "Descrição do Livro",
    "pages": "Número de páginas do Livro"
}

Resposta:
200 - Sucesso
{
	"id": "Id gerado",
	"name": "Nome do Livro",
	"author": "Autor do Livro",
	"description": "Descrição do Livro",
    "pages": "Número de páginas do Livro"
}

Caso esteja faltando algum dado obrigatório,
400 - Bad Request
{
    "message": "Informação do que está pendente"
}

##

8. /books/ (GET)
Body: No Body
Auth Types: No Authentication

Resposta:
200 - Sucesso
[
	{
	"id": "Id gerado",
	"name": "Nome do Livro",
	"author": "Autor do Livro",
	"description": "Descrição do Livro",
    "pages": "Número de páginas do Livro"
	},
	{
	"id": "Id gerado",
	"name": "Nome do Livro",
	"author": "Autor do Livro",
	"description": "Descrição do Livro",
    "pages": "Número de páginas do Livro"
	},
]

##

9. /books/:id/ (GET)
Body: No Body
Auth Types: No Authentication

Resposta:
200 - Sucesso
{
	"id": "Id gerado",
	"name": "Nome do Livro",
	"author": "Autor do Livro",
	"description": "Descrição do Livro",
    "pages": "Número de páginas do Livro"
	}

##

10. /books/:id/ (PATCH)
Body: Text Format - JSON
Auth Types: Bearer Token
Requisição:
{
    "campo(s)": "alteração"
}
Exemplo:
{
    "description": "Descrição do Livro"
}
Resposta:
200 - Sucesso
{
	"id": "Id gerado",
	"name": "Nome do Livro",
	"author": "Autor do Livro",
	"description": "Descrição do Livro",
    "pages": "Número de páginas do Livro"
	}

Caso esteja faltando algum dado obrigatório,
400 - Bad Request
{
    "message": "Informação do que está pendente"
}

Caso o id não seja encontrado
404 - Not Found
{
    "message": "user not found"
}

Caso o username cadastrado já exista,
409 - Conflit
{
	"message": "username already exists"
}

Caso o e-mail cadastrado já exista,
409 - Conflit
{
	"message": "email already exists"
}

##

11. /books/:id/follow/ (PATCH)
Body: No Body
Auth Types: Bearer Token

Resposta:
200 - Sucesso
{
"message": "Livro seguido com sucesso"
}

##

12. /books/:id/unfollow/ (DELETE)
Body: No Body
Auth Types: Bearer Token

Resposta:
200 - Sucesso
{
"message": "Deixou de seguir o Livro com sucesso"
}

##

13. /copy/:id/ (POST)
Body: Text Format - JSON
Auth Types: Bearer Token
Requisição:
{
    "book_id": id do livro no formato de number
}
Exemplo:
{
	"book_id": 2
}

Resposta:
200 - Sucesso
{
	"id": "id gerado formato de number",
	"is_available": "booleano que indica se o livro está disponível"
    "bood_id": "id do livro que foi separado"
}
Exemplo:
200 - Sucesso
{
	"id": 14,
	"is_available": true,
	"book_id": 2
}

Caso esteja faltando algum dado obrigatório,
400 - Bad Request
{
    "message": "Informação do que está pendente"
}

##

14. /copy/:id/ (GET)
Body: No Body
Auth Types: No Authentication

Resposta:
200 - Sucesso
[
{
	"id": "id gerado formato de number",
	"is_available": "booleano que indica se o livro está disponível"
    "bood_id": "id do livro que foi separado"
},
{
	"id": "id gerado formato de number",
	"is_available": "booleano que indica se o livro está disponível"
    "bood_id": "id do livro que foi separado"
}
]

## 

15. /loan/ (POST)
Body: Text Format - JSON
Auth Types: No Authentication
Requisição:
{
	"copy_id": id da separação do livro para empréstimo,
	"user_id": id do usuário que solicitou o empréstimo
}
Exemplo:
{
	"copy_id": 12,
	"user_id": 2
}

Resposta:
200 - Sucesso
{
	"id": id gerado,
	"copy_id": id da separação do livro para empréstimo,
	"user_id": id do usuário que solicitou o empréstimo,
	"created_date": "data de criação",
	"end_date": "prazo máximo para devolução",
	"book_returned": booleado que indica se o livro já foi devolvido
}

Exemplo:
200 - Sucesso
{
	"id": 29,
	"copy_id": 12,
	"user_id": 2,
	"created_date": "2023-07-11T18:21:26.271595Z",
	"end_date": "2023-07-17T18:21:26.271595Z",
	"book_returned": false
}

Caso esteja faltando algum dado obrigatório,
400 - Bad Request
{
    "message": "Informação do que está pendente"
}

##

16. /loan/ (GET)
Body: No Body
Auth Types: No Authentication

Resposta:
200 - Sucesso
[
    {
	"id": id gerado,
	"copy_id": id da separação do livro para empréstimo,
	"user_id": id do usuário que solicitou o empréstimo,
	"created_date": "data de criação",
	"end_date": "prazo máximo para devolução",
	"book_returned": booleado que indica se o livro já foi devolvido
},
{
	"id": id gerado,
	"copy_id": id da separação do livro para empréstimo,
	"user_id": id do usuário que solicitou o empréstimo,
	"created_date": "data de criação",
	"end_date": "prazo máximo para devolução",
	"book_returned": booleado que indica se o livro já foi devolvido
}
]

##

17. /loan/:id/ (PATCH) / *id do emprestimo (loan_id)
Body: No Body
Auth Types: No Authentication
Resposta:
200 - Sucesso
{
	"id": id gerado,
	"copy_id": id da separação do livro para empréstimo,
	"user_id": id do usuário que solicitou o empréstimo,
	"created_date": "data de criação",
	"end_date": "prazo máximo para devolução",
	"book_returned": booleado que indica se o livro já foi devolvido
}