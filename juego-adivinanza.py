import random

n_secreto = random.randint(1,100)
intentos = 0
intentos_max = 5
adivinando = False

print("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinando and intentos < intentos_max:
    
    #if not intentos > intentos_max:
        #print("No haz podido adivinar en 5 intentos.")
        #break
    
    numero = int(input("Ingrese un número del 1 al 99: \n-"))
    
    if numero == n_secreto:
        print("¡Felicitaciones haz adivinado el número secreto!")
        adivinando = True
    elif numero > n_secreto:
        print("El número es mayor al ingresado.")
    else:
        print("El número es menor al ingresado.")
    
    intentos += 1
    
if not intentos > intentos_max:
    print("No haz podido adivinar en 5 intentos.")
    
#if intentos >= intentos_max:
#    print("No haz podido adivinar en 5 intentos.")