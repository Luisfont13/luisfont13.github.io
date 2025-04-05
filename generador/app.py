from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/obtener_puntos', methods=['GET'])
def obtener_puntos():
    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)