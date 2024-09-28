#que la persoa vea cuál cola tenga menos gente.
#que los cajeros atiendan a las personas en su cola

import random
from faker import Faker #es un módulo que se instala con pip install faker
from cola import Cola

f = Faker()

fila_1 = Cola()
fila_2 = Cola()
fila_3 = Cola()

def filaMenosLlena():
    fila_a_elegir = 0
    personas_por_fila = [0] * 3
    personas_por_fila[0] = fila_1.tamano()
    personas_por_fila[1] = fila_2.tamano()
    personas_por_fila[2] = fila_3.tamano()

    comparador = 20
    for i in personas_por_fila:
        if i <= comparador:
            comparador = i

    indice = personas_por_fila.index(comparador)
    fila_a_elegir = indice+1

    return fila_a_elegir


i = 0
while True:
    i += 1
    persona = f.first_name() + "_" + f.last_name()
    num_cajero = filaMenosLlena()
    if num_cajero == 1:
        fila_1.agregar(persona)
        print(f"La persona {persona} fue agregada a la fila 1")
    if num_cajero == 2:
        fila_2.agregar(persona)
        print(f"La persona {persona} fue agregada a la fila 2")
    if num_cajero == 3:
        fila_3.agregar(persona)
        print(f"La persona {persona} fue agregada a la fila 3")
    
    if i == 15:
        break

print("Fila 1", fila_1.items)
print("Fila 2", fila_2.items)
print("Fila 3", fila_3.items)

def atender():
    while True:
        numCajero = random.randrange(1,4)
        if numCajero == 1:
            if not fila_1.estaVacia():
                print("Se atendió a: ", fila_1.avanzar())
        elif numCajero == 2:
            if not fila_2.estaVacia():
                print("Se atendió a: ", fila_2.avanzar())
        elif numCajero == 3:
            if not fila_3.estaVacia():
                print("Se atendió a: ", fila_3.avanzar())
        
        if fila_1.estaVacia() and fila_2.estaVacia() and fila_3.estaVacia():
            break

atender()