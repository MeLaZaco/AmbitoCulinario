from flask import Flask, render_template
from models.ambitoculinario import ambitoculinarios

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #search = request.args.get('search')
    #if search:
        #print("search parameter: " + search)

    return render_template('index.html')

@app.route('/producto.html/', methods=['GET'])
def producto():
    return render_template('producto.html')

@app.route('/', methods=['POST'])
def hello_world_post():
    return 'Hello, World! POST'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
