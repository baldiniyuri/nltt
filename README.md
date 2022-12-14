# NLTT

## Instalation
```

Criar o arquivo ENV com as seguintes variáveis de ambiente.

DB_HOST
DB_NAME
DB_USER
DB_PASS
SECRET_KEY
THROTTLE_ANON
THROTTLE_USER
ALLOWED_HOSTS
RESIZE_URL

Depois executar o comando.

Para ambiente local 
docker-compose build

Para ambiente de produção
docker-compose -f docker-compose-deploy.yml build
```

## Run

```
Rodar o servidor Localmente
docker-compose up

Rodar o servidor de Produção
docker-compose -f docker-compose-deploy.yml up
```

## Tests

```
docker-compose run --rm app sh -c "python manage.py test"
```

### Post api/register/

Porta 8000
```Request post para registrar usuário.

Post Json
{
	"email": "email@teste.com",
	"password": "123456"
}

// RESPONSE STATUS -> HTTP 201
{
  "data": {
    "id": 1,
    "email": "email@teste.com",
    "is_staff": false,
    "is_superuser": false
  },
  "token": "ffd213ee97bf14cbd824c9509f8737a01f9ff005"
}
```

### GET api/get-user-data/<int:user_id>/

Porta 8000
```Request post para pegar os dados do usuário.

HEADERS {Authentication Token tokenhash}

// RESPONSE STATUS -> HTTP 200
{
  "id": 2,
  "email": "teste@email.com",
  "is_staff": false,
  "is_superuser": false
}
```


### Post api/images-to-resize/

Porta 8000
```Request post para redimencionar imagens.

Post Multipart Form

HEADERS {Authentication Token tokenhash}
{
	"user_id": 1,
	"image": "123456",
}
// RESPONSE STATUS -> HTTP 201
```

### GET api/images/<int:user_id>/

Porta 8000
```Request get para pegar as imagens do usuário.

HEADERS {Authentication Token tokenhash}

// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "image": "/static/media/rio-grade_sul.jpg",
    "user_id": 1
  }
]
```