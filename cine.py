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
        self.salas = salas if isinstance(salas, list) else []

    

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

                
            
    def isolate_objetos(self, data):
        from CRUD import CRUD
        crud = CRUD()
        for c in data:
            salas = Sala()
            salas.isolate_objetos(c["salas"])
            
            if not salas.informacion:
                c["salas"] = salas
                cine = Cine(nombre=c["nombre"], ubicacion=c["ubicacion"], hora_apertura=c["hora_apertura"], 
                            hora_cierre=c["hora_cierre"], numplantas=c["numplantas"], salas=c["salas"])
                crud.agregar(cine)
                self.informacion_iso.append(cine)      
                
                
    # CONSOLA

if __name__ == "__main__":
    from sala import Sala
    from CRUD import CRUD
    
    cines = Cine()
    data = cines.read_json("json/cines.json")
    cines.isolate_objetos(data) 
    for c in cines.informacion_iso:
        print(type(c))
    
    
    
    
    
    
            
