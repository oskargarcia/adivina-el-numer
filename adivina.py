# simple pero la idea esevolucionarlo hasta un cuestionario ;)
print("hola adivina la respuesta correcta")
while True:
  n=int(input('cual es el numero '))
  # define el numer a adivinar en la linea de abajo n==" "
  if n==5:
    print('felicidades adivinaste')
    break
  elif n<5:
    print('tu numero es menor')
  else:
    print('tu numero es es mayor')