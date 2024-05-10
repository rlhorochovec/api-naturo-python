# api-naturo-python

Projeto de API utilizando Python com Flask e SQLite.

## Rodando localmente

```bash
    cd api-naturo-python
    pip install Flask 
    pip install Flask-Cors 
    python api.py
```

## Acessando

```
http://localhost:5000/api/naruto
```

## Documentação da API

#### Insere um ninja

```
  POST /api/naruto/add
```

| Parâmetro | Tipo      | Descrição                                      |
| :-------- | :-------- | :--------------------------------------------- |
| `name`    | `string`  | **Obrigatório**. O nome do ninja que você quer |
| `village` | `string`  | **Obrigatório**. A vila que o ninja pertence   |

#### Retorna todos os ninjas

```
  GET /api/naruto
```

#### Retorna um ninja

```
  GET /api/naruto/${id}
```

| Parâmetro | Tipo       | Descrição                                    |
| :-------- | :--------- | :------------------------------------------- |
| `id`      | `integer`  | **Obrigatório**. O ID do ninja que você quer |


#### Altera um lutador

```
  PUT /api/naruto/update
```

| Parâmetro | Tipo      | Descrição                                      |
| :-------- | :-------- | :--------------------------------------------- |
| `id`      | `integer` | **Obrigatório**. O ID do ninja que você quer   |
| `name`    | `string`  | **Obrigatório**. O nome do ninja que você quer |
| `village` | `string`  | **Obrigatório**. A vila que o ninja pertence   |

#### Remove um lutador

```
  DEL /api/naruto/delete/2
```

| Parâmetro | Tipo       | Descrição                                    |
| :-------- | :--------- | :------------------------------------------- |
| `id`      | `integer`  | **Obrigatório**. O ID do ninja que você quer |