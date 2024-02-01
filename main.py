from CRUD import CRUD
from cine import Cine
from sala import Sala
from Funcion import Funcion

# salas = Sala()
# data = salas.read_json("json/salas.json")
# salas.isolate_objetos(data)
# for s in salas.informacion_iso:
#     print(type(s))
#     print(type(s.funciones))
#     for f in s.funciones.informacion_iso:
#         print(type(f))


# cines = Cine()
# data = cines.read_json("json/cines.json")
# cines.isolate_objetos(data) 
# for c in cines.informacion_iso:
#     print(type(c))
#     print(type(c.salas))
#     for s in c.salas.informacion_iso:
#         print(type(s))
#         print(type(s.funciones))
#         for f in s.funciones.informacion_iso:
#             print(type(f))
            




funcion1 = Funcion(2, "08:10", "Spiderman", "08/01/2024", "10:20", 70)
funcion2 = Funcion(3, "10:10", "Superman", "10/01/2024", "12:20", 90)
sala1 = Sala("b1", 150, "08:00", 200, [funcion1, funcion2])
cine1 = Cine("Sexmex", "San Pedro Sula", "08:00", "22:00", [sala1], 20)

funciones=Funcion()

crud = CRUD()
crud.agregar(cine1)
print(crud.to_dictionary())
crud.save_json(data=crud.to_dictionary())