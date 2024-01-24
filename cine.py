from CRUD import CRUD
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
            salas_str = "\n".join([str(sala) for sala in self.salas]) if self.salas else "No hay salas"
            return f"nombre: {self.nombre}\nubicacion: {self.ubicacion}\nhora_apertura: {self.hora_apertura}\nhora_cierre: {self.hora_cierre}\nnumplantas: {self.numplantas}\n\nsalas: {salas_str}"
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



