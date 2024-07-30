from flask import Flask, render_template
from models.informacion_producto import informacion_producto

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #search = request.args.get('search') 
    #if search:
       # print("search parameter: " + search)
      #  gatos = informacion_producto.get_all_filter(search)
   # else:
      #  gatos = informacion_producto.get_all()
    return render_template("index.html", informacion_producto=informacion_producto)

@app.route('/', methods=['GET'])
def producto():
    return render_template('producto.html')

@app.route('/', methods=['POST'])
def hello_world_post():
    return 'Hello, World! POST'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
