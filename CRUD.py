# VERSION MAS RECIENTE
import json

class CRUD:
    def __init__(self):
        self.informacion = []
        self.informacion_iso = []

    def agregar(self, instancia):
        self.informacion.append(instancia)

    def showIndex(self, index):
        if 0 <= index < len(self.informacion):
            return self.informacion[index]
        else:
            print("No se encontró ninguna función con ese ID.")
        
        
    def show(self):
        print(self.informacion)
        for i in self.informacion:
            print(i)
            
    def show_objects(self):
        for i in self.informacion_iso:
            print(i)
           
#*
    def modificar(self, indice, instancia):
        if 0 <= indice < len(self.informacion):
            self.informacion[indice] = instancia
            return True
        else:
            return False
#*


#*
    def eliminar(self, indice):
        if 0 <= indice < len(self.informacion):
            del self.informacion[indice]
            return True
        else:
            return False
#*

    def to_dictionary(self):
        if len(self.informacion) == 0:
            return []
        else:
            dict_list = []

            for elemento in self.informacion:
                if hasattr(elemento, 'to_dictionary') and callable(getattr(elemento, 'to_dictionary')):
                    dict_list.append(elemento.to_dictionary())
                else:
                    dict_list.append(vars(elemento))

            return dict_list
  
    def read_json(slef, json_data = "json/informacionJSON.json"):
        try:
            with open(json_data, 'r') as archivo:
                data = json.load(archivo)
                return data
        except:
            return []
        
                       
    def populate_object(self, obj, data, attributes):
        for attribute in attributes:
            setattr(obj, attribute, data.get(attribute, None))
            

        
    def save_json(self, archivo="json/informacionJSON.json", data=None):
        try:
            with open(archivo, "r") as file:
                existing_data = json.load(file)

        except:
            existing_data = []

        existing_data_set = set(json.dumps(item) for item in existing_data)

        for item in data:
            item_json = json.dumps(item)
            if item_json not in existing_data_set:
                existing_data.append(item)
                existing_data_set.add(item_json)
        with open(archivo, "w") as file:
            json.dump(existing_data, file, indent=4, default=lambda x: 
                x.to_dict() if hasattr(x, 'to_dict') else x)
            
        



    def save_to_json(self, filename="json/informacionJSON.json"):
        if self.read_json() == []:
            dict_list = [elemento.to_dictionary() for elemento in self.informacion]
            with open(filename, 'w') as archivo:
                json.dump(dict_list, archivo, indent=4)