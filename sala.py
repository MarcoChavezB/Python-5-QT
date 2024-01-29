from CRUD import CRUD
from Funcion import Funcion
class Sala(CRUD):
    def __init__(self, numero=None, num_asientos=None, hora_limpieza=None, max_personas=None, funciones=None):
        super().__init__()
        self.numero = numero
        self.num_asientos = num_asientos
        self.hora_limpieza = hora_limpieza
        self.max_personas = max_personas
        self.funciones = funciones

    def __str__(self):
        if not self.informacion:
            funciones_str = "\n".join([str(funcion) for funcion in self.funciones]) if self.funciones else ""
            return (
                f"numero: {self.numero},\n"
                f"num_asientos: {self.num_asientos},\n"
                f"hora_limpieza: {self.hora_limpieza},\n"
                f"max_personas: {self.max_personas},\n\n"
                f"funciones: {funciones_str}"
            )
        else:
            elementos_str = [str(elemento) for elemento in self.informacion]
            return "\n".join(elementos_str)


    def to_dictionary(self):
        if not self.informacion:
            return {
                'numero': self.numero,
                'num_asientos': self.num_asientos,
                'hora_limpieza': self.hora_limpieza,
                'max_personas': self.max_personas,
                'funciones': [funcion.to_dictionary() for funcion in self.funciones] if self.funciones else None 
            }
        else:
            return None
        
        
        
    def isolate_objetos(self,data):
        for d in data:
                funciones = Funcion()
                funciones.isolate_funciones_objetos(d["funciones"])
                d["funciones"]=funciones
                sala = Sala(numero=d["numero"],num_asientos=d["num_asientos"],hora_limpieza=d["hora_limpieza"],max_personas=d["max_personas"],funciones=d["funciones"])
                self.informacion_iso.append(sala)
        
        
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def json_to_object (self):
        print("Sala ejecutada")
        from Funcion import Funcion
        from cine import Cine
        
        datos = self.read_json()
        
        for cine_data in datos:
            print("cines")
            cine = Cine()
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
        
            for sala_data in cine_data['salas']:
                sala = Sala()
                self.populate_object(sala, sala_data, ['numero', 'num_asientos', 'hora_limpieza', 'max_personas'])                
                self.informacion_iso.append(sala)
                funcion = Funcion()
                funcion.json_to_object()
        return self.informacion_iso
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    def isolate_sala_data(self):
        from cine import Cine
        from Funcion import Funcion
        
        datos = self.read_json()    
        
        for cine_data in datos:
            cine = Cine()
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
        
            for data in cine_data['salas']:
                sala = Sala()
                self.populate_object(sala, data, ['numero', 'num_asientos', 'hora_limpieza', 'max_personas'])
                self.informacion_iso.append(sala)        
        return self.informacion_iso
    
    
if __name__ == "__main__":
    from Funcion import Funcion
    from sala import Sala
    from cine import Cine

    crud = CRUD()

    funcion1 = Funcion(1, "08:10", "spiderman", "08/01/2024", "10:20", 70)
    funcion2 = Funcion(3, "10:10", "Superman", "10/01/2024", "12:20", 90)
    sala1 = Sala("b1", 150, "08:00", 200, [funcion1, funcion2])
    cine1 = Cine("Cinemex", "Torreon", "08:00", "22:00", [sala1], 3)


    funcion3 = Funcion(2, "09:30", "Avengers", "09/01/2024", "11:45", 80)
    funcion4 = Funcion(4, "12:00", "Batman", "11/01/2024", "14:15", 100)
    sala2 = Sala("c1", 120, "09:00", 180, [funcion3, funcion4])
    cine2 = Cine("Cinepolis", "Torreon", "08:30", "21:30", [sala2], 2)

    cines = Cine()
    cines.agregar(cine1)
    cines.agregar(cine2)
    
    sala1.json_to_object()
    sala1.show_isolate()
