# importar la función que devolverá una instancia de una conexión
from config.db import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class ambitoculinarios:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tareas;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('ambitoculinario').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append( cls(friend) )
        return friends
    
    def insertar_tareas(cls,data):
        query = "INSERT INTO ambitoculinario (nombre VALUES (%(ambitoculinario)s);"
        print(data)
        return connectToMySQL('ambitoculinario').query_db(query, data=data)
#buscador
    @classmethod
    def get_all_filter(cls, search_team):
        query = f"select"