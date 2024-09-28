# archivo: app.py
from flask import Flask
import os

app = Flask(__name__)

# Endpoint 'bueno' que responde con un mensaje de éxito
@app.route('/good')
def bueno():
    return "Todo va bien en /bueno"

# Endpoint 'malo' que forzará el cierre del contenedor
@app.route('/bad')
def malo():
    # Forzar el fallo del contenedor
    os._exit(1)  # Matar el proceso principal y apagar el contenedor
    return "Esto no debería ser visto, el contenedor se apaga."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
