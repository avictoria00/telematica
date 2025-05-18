from flask import Flask

app = Flask(__name__)

@app.route('/')
def mensaje():
    return 'profe hola, como estas? este es mi mejor intento de pa pagina jeje D:. Muchisimas gracias por todo :)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
