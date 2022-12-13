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

Depois executar o comando.

docker-compose build
```

## Run

```
docker-compose up
```

## Tests

```
docker-compose run --rm app sh -c "python manage.py test"
```