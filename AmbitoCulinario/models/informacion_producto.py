# importar la función que devolverá una instancia de una conexión
from config.db import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class informacion_producto:
    def __init__( self , data ):
        self.id_informacion_producto = data["id_informacion_producto"]
        self.imagen_producto = data["imagen_producto"]
        self.marca_producto = data["marca_producto"]
        self.nombre_producto = data["nombre_producto"]
        self.precio_producto = data["precio_producto"]
        self.porcentaje_quitado = data["porcentaje_quitado"]
        self.precio_original = data["precio_original"]
        self.pais_origen = data["pais_origen"]
        self.condicion_producto = data["condicion_producto"]
        self.modelo_producto = data["modelo_producto"]
        self.material_producto = data["material_producto"]
        self.espesor_producto = data["espesor_producto"]
        self.tipo_utensilio_producto = data["tipo_utensilio_producto"]
        self.dimension_producto = data["dimension_producto"]
        self.uso_producto = data["uso_producto"]
        self.garantia_producto = data["garantia_producto"]
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM informacion_productos;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('ambitoculinario').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append( cls(friend) )
        return friends
    
    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM informacio_producto WHERE nombre LIKE '%{search_term}%';"
        results = connectToMySQL('ambitoculinario').query_db(query)
        productitos = []
        for result in results:
            productitos.append(cls(result))
        return productitos
#buscador
    #@classmethod
    #def get_all_filter(cls, search_team):
        #query = f"select"