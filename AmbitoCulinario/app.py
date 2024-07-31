from flask import Flask, render_template, request
from models.informacion_productos import Producto

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    #productos = Producto.get_all_limit_all(1)
    return render_template("index.html") #productos=productos)

@app.route('/AmbitoCulinario/templates/producto.html', methods=['GET'])
def Info():
    return render_template("producto.html")

@app.route('/AmbitoCulinario/templates/producto2.html', methods=['GET'])
def Info1():
    return render_template("producto2.html")

@app.route('/AmbitoCulinario/templates/producto3.html', methods=['GET'])
def Info2():
    return render_template("producto3.html")

@app.route('/AmbitoCulinario/templates/producto4.html', methods=['GET'])
def Info3():
    return render_template("producto4.html")

@app.route('/AmbitoCulinario/templates/producto5.html', methods=['GET'])
def Info4():
    return render_template("producto5.html")

@app.route('/AmbitoCulinario/templates/producto6.html', methods=['GET'])
def Info5():
    return render_template("producto6.html")

@app.route('/AmbitoCulinario/templates/producto1.html', methods=['GET'])
def Info6():
    return render_template("producto1.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8090)