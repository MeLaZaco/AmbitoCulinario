from flask import Flask, render_template
from models.informacion_producto import informacion_producto

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    search = request.args.get('search') 
    if search:
        print("search parameter: " + search)
        gatos = Gato.get_all_filter(search)
    else:
        gatos = Gato.get_all()
    return render_template("index.html", gatos=gatos, search=search)

@app.route('/', methods=['GET'])
def producto():
    return render_template('producto.html')

@app.route('/', methods=['POST'])
def hello_world_post():
    return 'Hello, World! POST'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
