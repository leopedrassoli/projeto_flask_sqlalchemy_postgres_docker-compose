from database import init_db
from flask import Flask, request, json, jsonify
from models import *
from database_utils import *

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'


@app.route('/hello')
def api_hello(): 
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:        
        return 'Hello John Doe'


@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


@app.route('/user', methods=['POST', 'DELETE', 'GET', 'PUT'])
def api_user():
    data = json.loads(request.data.decode('utf-8'))
    if request.method == 'POST':
        try:
            add_user(data)
            res = {'status': 'User criado'}
        except Exception:
            res = {'status': 'Erro'}
        return jsonify(res)
    elif request.method == 'GET':
        if 'name' in data:
            try:
                res = get_user(data)
            except Exception:
                res = {'status': 'Erro'}
            return jsonify(res)
        else:
            try:
                res = get_users()
            except Exception:
                res = {'status': 'Erro'}
            return jsonify(res)
    elif request.method == 'DELETE':
        try:
            res = delete_user(data)
            res = {'status': 'User removido'}
        except Exception:
            res = {'status': 'Erro'}
        return jsonify(res)
    elif request.method == 'PUT':
        try:
            res = edit_user(data)
            res = {'status': 'User editado'}
        except Exception:
            res = {'status': 'Erro'}
        return jsonify(res)
    else:
        res = {'status': 'Comando nao identificado'}
        return jsonify(res)


@app.route('/course', methods=['POST', 'DELETE', 'GET', 'PUT'])
def api_course():
    data = json.loads(request.data.decode('utf-8'))
    if request.method == 'POST':
        try:
            add_course(data)
            res = {'status': 'Course criado'}
        except Exception:
            res = {'status': 'Erro'}
        return jsonify(res)
    elif request.method == 'GET':
        if 'description' in data:
            try:
                res = get_course(data)
            except Exception:
                res = {'status': 'Erro'}
            return jsonify(res)
        else:
            try:
                res = get_courses()
            except Exception:
                res = {'status': 'Erro'}
            return jsonify(res)
    elif request.method == 'DELETE':
        try:
            res = delete_course(data)
            res = {'status': 'Course removido'}
        except Exception:
            res = {'status': 'Erro'}
        return jsonify(res)
    elif request.method == 'PUT':
        try:
            res = edit_course(data)
            res = {'status': 'Course editado'}
        except Exception:
            res = {'status': 'Erro'}
        return jsonify(res)
    else:
        res = {'status': 'Comando nao identificado'}
        return jsonify(res)


@app.route('/grade', methods=['POST', 'DELETE', 'GET'])
def api_grade():
    data = json.loads(request.data.decode('utf-8'))
    if request.method == 'POST':
        try:
            add_grade(data)
            res = {'status': 'Grade criada'}
        except Exception:
            res = {'status': 'Erro'}
        return jsonify(res)
    elif request.method == 'GET':
        if 'idCourse' in data and 'idUser' in data:
            try:
                res = get_grade(data)
            except Exception:
                res = {'status': 'Erro'}
        else:
            try:
                res = get_grades()
            except Exception:
                res = {'status': 'Erro'}
        return jsonify(res)
    elif request.method == 'DELETE':
        try:
            res = delete_grade(data)
            res = {'status': 'Grade removida'}
        except Exception:
            res = {'status': 'Erro'}
        return jsonify(res)
    else:
        res = {'status': 'Comando nao identificado'}
        return jsonify(res)


@app.route('/report', methods = ['GET']) 
def api_report():
    try:
        res = get_report()
    except Exception:
            res = {'status': 'Erro'}
    return jsonify(res)


if __name__ == '__main__':
    init_db()
    app.run(host='172.20.0.5', port=5000, debug=True)