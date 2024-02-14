from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, connection_string="URLCONECTION", database_name="cinema", collection_name="cine"):
        try:
            print("Conectando a la base de datos...")
            self.client = MongoClient(connection_string)
            self.db = self.client[database_name]
            self.collection = self.db[collection_name]
            print("Conexión exitosa")
        except:
            print("Error al conectarse a la base de datos")
            
    def insert(self, data):
        try:
            self.collection.insert_many(data)
            print("Datos guardados en MongoDB")
        except:
            print("Error al guardar datos en MongoDB")
        

