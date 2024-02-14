from CRUD import CRUD
from sala import Sala
class Cine(CRUD):
    def __init__(self, nombre=None, ubicacion=None, hora_apertura=None, hora_cierre=None, salas=None, numplantas=None):
        super().__init__()
        self.informacion = []
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.numplantas = numplantas
        self.salas = salas if salas is not None else []

    

    def __str__(self):
        if not self.informacion:
            salas_str = "\n".join([str(sala) for sala in self.salas.informacion]) if self.salas else ""
            return (
                f"\n nombre: {self.nombre}\n"
                f"ubicacion: {self.ubicacion}\n"
                f"hora_apertura: {self.hora_apertura}\n"
                f"hora_cierre: {self.hora_cierre}\n"
                f"numplantas: {self.numplantas}\n\n"
                f"salas: {salas_str}" 
            )
        else:
            elementos_str = [str(elemento) for elemento in self.informacion]
            return "\n".join(elementos_str)

        
    def to_dictionary(self):
        if not self.informacion:
            return {
                'nombre': self.nombre,
                'ubicacion': self.ubicacion,
                'hora_apertura': self.hora_apertura,
                'hora_cierre': self.hora_cierre,
                'numplantas': self.numplantas,
                'salas': [sala.to_dictionary() for sala in self.salas.informacion] if self.salas else None
            }
        else:
            return None

                
            
    # def isolate_objetos(self, datos):
    #     from sala import Sala
    #     from Funcion import Funcion        
    #     for cine_data in datos:
    #         cine = Cine()
    #         self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
    #         self.informacion.append(cine)

    #         for dataSala in cine_data['salas']:
    #             sala = Sala()
    #             self.populate_object(sala, dataSala, ['numero', 'num_asientos', 'hora_limpieza', 'max_personas'])
    #             self.informacion.append(sala)

    #             for dataFuncion in dataSala['funciones']:
    #                 funcion = Funcion()
    #                 self.populate_object(funcion, dataFuncion, ['Nfuncion', 'hora_inicio', 'pelicula', 
    #                                                             'fecha_estreno', 'hora_fin', 'costo_boleto'])
    #                 self.informacion.append(funcion)
    #     return self.informacion
    
    
    def isolate_objetos(self, datos):
        for cine_data in datos:
            cine = Cine()
            sala = Sala()
            sala.isolate_objetos(cine_data["salas"])
            cine.nombre = cine_data["nombre"]
            cine.ubicacion = cine_data["ubicacion"]
            cine.hora_apertura = cine_data["hora_apertura"]
            cine.hora_cierre = cine_data["hora_cierre"]
            cine.numplantas = cine_data["numplantas"]
            cine.salas = sala
            self.informacion.append(cine)
    
    # def isolate_objetos(self, data):
    #     for d in data:
    #         sala = Sala()
    #         sala.isolate_objetos(d["salas"])
    #         cine = Cine(
    #             nombre=d["nombre"],
    #             ubicacion=d["ubicacion"],
    #             hora_apertura=d["hora_apertura"],
    #             hora_cierre=d["hora_cierre"],
    #             numplantas=d["numplantas"],
    #             salas=sala
    #         )
    #         self.informacion.append(cine)
            
        
    # CONSOLA

if __name__ == "__main__":
    from sala import Sala
    from CRUD import CRUD
    
    cines = Cine()
    data = cines.read_json("json/cines.json")
    cines.isolate_objetos(data) 
    for c in cines.informacion_iso:
        print(type(c))
    
    
    
    
    
    
            
