"""
API REST con Flask — Ejercicio 1

Descripción:
    Este programa implementa una API REST básica utilizando el framework Flask de Python.
    La API expone tres endpoints que permiten interactuar con datos de usuarios:

    1. GET  /              → Retorna un saludo "Hola Mundo" (endpoint de prueba).
    2. GET  /users/<id>    → Retorna un JSON con los datos de un usuario dado su ID.
                             Acepta un parámetro de consulta opcional '?query=' que se
                             incluye en la respuesta si está presente.
    3. POST /users         → Recibe un JSON en el cuerpo de la petición con datos de
                             un nuevo usuario y lo retorna con un código 201 (Created).

Lo que aprendí en este ejercicio:
    En este ejercicio aprendí los fundamentos para crear una API REST utilizando Flask.
    Comprendí cómo definir rutas (endpoints) con distintos métodos HTTP (GET y POST),
    cómo recibir parámetros dinámicos en la URL (como el ID del usuario), cómo leer
    query parameters con request.args, y cómo manejar el envío y recepción de datos
    en formato JSON usando jsonify() y request.get_json(). También aprendí a devolver
    códigos de estado HTTP apropiados (200 para éxito, 201 para recurso creado).
    Finalmente, utilicé Postman como herramienta para probar cada endpoint de la API,
    lo cual me permitió verificar que las respuestas fueran correctas sin necesidad
    de crear un frontend.

Autor: Estudiante
Fecha: Marzo 2026
"""

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo'

@app.route('/users/<user_id>')
def get_user(user_id):
    user = {
        'id': user_id,
        'name': 'John Doe',
        'telefono': '1234567890'
    }
    query = request.args.get('query')
    if query:
        user['query'] = query
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True)