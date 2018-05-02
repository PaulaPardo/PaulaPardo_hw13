import numpy as np
import random 

# Crea una lista y la retorna desordenada aleatoriamente
def sort_doors():
    lista = ['goat', 'goat', 'car']
    return random.sample(lista, len(lista))

# Retorna un numero aleatorio entre [0,1,2]
def choose_door():
    return np.random.choice(3,1)[0]

# Recorre la lista en los espacios que no incluyen a choice y cuando encuentra la primera cabra, para y modifica su valor por 'GOAT_MONTY'
def reveal_door(lista, choice):
    for i in range(len(lista)):
        if(i != choice):
            if(lista[i] == 'goat'):
                lista[i] = 'GOAT_MONTY'   
                break
    return lista

# Retorna el valor de la lista que no esta en la posicion choice y TAMPOCO es 'GOAT_MONTY'
def finish_game(lista, choice, change):
    if(change == False):
        a = lista[choice]
    else:
        for i in range(len(lista)):
            if(lista[i] != lista[choice]) and (lista[i] != 'GOAT_MONTY'):
                a = lista[i]
    return a


# Se simulan muchos escenarios del juego:

listaFalse = []
listaTrue = []

for i in range(99):

    l = sort_doors()
    c = choose_door()
    l2 = reveal_door(l,c)
    resultado = finish_game(l2,c,False)
    listaFalse.append(resultado)

for j in range(99):

    l = sort_doors()
    c = choose_door()
    l2 = reveal_door(l,c)
    resultado = finish_game(l2,c,True)
    listaTrue.append(resultado)

a = np.where(np.array(listaFalse) == 'car')
b = np.where(np.array(listaTrue) == 'car')

print len(listaFalse)

print "La probabilidad de obtener el premio sin cambio de puerta es: ", (len(a[0])+0.0)/len(listaFalse)
print "La probabilidad de obtener el premio con cambio de puerta es: ", (len(b[0])+0.0)/len(listaTrue)


    
    
