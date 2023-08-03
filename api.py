"""
API - lugar para disponibilizar recursos ou funcionalidades
1 - objetivo - CRUD livros
2 - url base - localhost
3 - endpoints - localhost/livros(get), localhost/livros(post), localhost/livros/id(get), localhost/livros/id(PUT), localhost/livros/id(delete)
4 - quais recursos - livros
"""

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client.livraria

collection = db.livros


from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis',
        'Autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry potter',
        'Autor': 'J.K HOWLING'
    },
]

collection.insert_one(livros)


def inserir_dados():
    collection.insert_one(livros)



@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return livro


@app.route('/livros/<int:id>', methods=['PUT'])
def alterar_livros_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


@app.route('/livros/<int:id>', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    collection.insert_one(livros)
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)
