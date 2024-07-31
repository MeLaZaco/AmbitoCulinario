from flask import Flask, render_template, request
from models.informacion_productos import Producto

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    search = request.args.get('search') 
    if search:
        print("search parameter: " + search)
        informacion_productos = Producto.get_all_filter(search)
    else:
        informacion_productos = Producto.get_all()
    return render_template("index.html", informacion_productos=informacion_productos, search=search)

@app.route('/', methods=['GET'])
def producto():
    producto = Producto.get_producto()
    return render_template("index.html", producto=producto[0])

@app.route('/producto.html', methods=['GET'])
def Info():
    return render_template("producto.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8090)