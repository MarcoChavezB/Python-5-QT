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
        self.salas = salas

    def __str__(self):
        if not self.informacion:
            salas_str = "\n".join([str(sala) for sala in self.salas]) if self.salas else ""
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
                'salas': [sala.to_dictionary() for sala in self.salas] if self.salas else None
            }
        else:
            return None

        
    def isolate_cine_data(self):
        datos = self.read_json()
        for cine_data in datos:
            cine = Cine()
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
            self.informacion_iso.append(cine)
            
                    
    def isolate_all_data(self):
        from sala import Sala
        from Funcion import Funcion

        datos = self.read_json()            
        for cine_data in datos:
            cine = Cine()
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
            self.informacion_iso.append(cine)
            
            for dataSala in cine_data['salas']:
                sala = Sala()
                self.populate_object(sala, dataSala, ['numero', 'num_asientos', 'hora_limpieza', 'max_personas'])
                self.informacion_iso.append(sala)
                
                for dataFuncion in dataSala['funciones']:
                    funcion = Funcion()
                    self.populate_object(funcion, dataFuncion, ['Nfuncion', 'hora_inicio', 'pelicula', 
                                                                'fecha_estreno', 'hora_fin', 'costo_boleto'])
                    self.informacion_iso.append(funcion)
        return self.informacion_iso
    
    
    
    def isolate_recursiva(self):
        datos = self.read_json()
        for cine_data in datos:
            cine = Cine()
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
            self.informacion_iso.append(cine)
            
            
            
            
            
            
            
            
    
            
            
    def isolate_objetos(self, data):
        for c in data:
            salas = Sala()
            salas.isolate_objetos(c["salas"])
            c["salas"] = salas
            cine = Cine(nombre=c["nombre"], ubicacion=c["ubicacion"], hora_apertura=c["hora_apertura"], 
                        hora_cierre=c["hora_cierre"], numplantas=c["numplantas"], salas=c["salas"])
            self.informacion_iso.append(cine)
