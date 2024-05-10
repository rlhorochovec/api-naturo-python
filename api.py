from database.sqlite_config import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/naruto', methods=['GET'])
def api_get_ninjas():
    return jsonify(get_ninjas())

@app.route('/api/naruto/<id>', methods=['GET'])
def api_get_ninja(id):
    return jsonify(get_ninja_by_id(id))

@app.route('/api/naruto/add',  methods = ['POST'])
def api_add_ninja():
    ninja = request.get_json()
    return jsonify(insert_ninja(ninja))

@app.route('/api/naruto/update',  methods = ['PUT'])
def api_update_ninja():
    ninja = request.get_json()
    return jsonify(update_ninja(ninja))

@app.route('/api/naruto/delete/<id>',  methods = ['DELETE'])
def api_delete_ninja(id):
    return jsonify(delete_ninja(id))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run()