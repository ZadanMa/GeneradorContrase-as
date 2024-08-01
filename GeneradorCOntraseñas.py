import random
letras = ["a","b","c","d","e","f","g","h","i","j","k",
          "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]
simbolos = ["!","@","#","$","%","^","&","*","(",")","_","+","="]
print("Bienvenidos a tu generador de contraseñas")
letraPass = int(input("Cuantas letras debe tener tu contraseña?\n"))
simbolosPass = int(input("Cuantas simbolos debe tener tu contraseña?\n"))
numerosPass = int(input("Cuantas numeros debe tener tu contraseña?\n"))
contraseña = []
for i in range(1, letraPass + 1):
    #choise sirve para elegir una letra aleatoria
    contraseña +=random.choice(letras)
for i in range(1, simbolosPass + 1):
    contraseña +=random.choice(simbolos)
for i in range(1, numerosPass + 1):
    contraseña +=random.choice(numeros)
#shuffle desordenada los valores de la lista
random.shuffle(contraseña)
#join uno los valores de la lista en una cadena de caracteres
contraseña1 = "".join(contraseña)
print(contraseña1)
