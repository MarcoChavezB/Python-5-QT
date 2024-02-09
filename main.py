from cine import Cine
from sala import Sala
from Funcion import Funcion
from CRUD import CRUD


funcion1 = Funcion(2, "08:10", "Spiderman", "08/01/2024", "10:20", 70)
funcion2 = Funcion(3, "10:10", "Superman", "10/01/2024", "12:20", 90)
sala1 = Sala("b1", 150, "08:00", 200, [funcion1, funcion2])
cine1 = Cine("Sexmex", "San Pedro Sula", "08:00", "22:00", [sala1], 20)
cine2 = Cine("Cinemex", "San Pedro Sula", "08:00", "22:00", [sala1], 20)

crud = CRUD()
crud.agregar(cine1)
crud.agregar(cine2)

crud.show()
crud.eliminar(0)
print("-------------------------------")
crud.show()



# crud.modificar(0, Cine("NEW CINEMA", "San Pedro Sula", "08:00", "22:00", [sala1], 20))    