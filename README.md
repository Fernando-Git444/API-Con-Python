# API REST con Flask — Ejercicio 1

API REST básica construida con Python y Flask que permite gestionar datos de usuarios.

## Requisitos

- Python 3.x
- Flask

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

El servidor se iniciará en `http://127.0.0.1:5000`.

## Endpoints

| Método | Ruta              | Descripción                          |
|--------|-------------------|--------------------------------------|
| GET    | `/`               | Retorna "Hola Mundo"                 |
| GET    | `/users/<id>`     | Retorna datos de un usuario por ID   |
| POST   | `/users`          | Crea un nuevo usuario (recibe JSON)  |

### Ejemplos

**GET /users/1**
```json
{
  "id": "1",
  "name": "John Doe",
  "telefono": "1234567890"
}
```

**GET /users/1?query=test**
```json
{
  "id": "1",
  "name": "John Doe",
  "telefono": "1234567890",
  "query": "test"
}
```

**POST /users** (Body JSON)
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

## Evidencia

Las capturas de pantalla de las pruebas realizadas con Postman se encuentran en la carpeta `screenshots/`.

## Lo que aprendí

En este ejercicio aprendí los fundamentos para crear una API REST utilizando Flask: definir rutas con distintos métodos HTTP (GET y POST), recibir parámetros dinámicos en la URL, leer query parameters, y manejar datos en formato JSON. También aprendí a utilizar Postman para probar y verificar cada endpoint de la API.
