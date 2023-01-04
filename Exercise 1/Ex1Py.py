def val_ai(num):
  try: num = int(num)
  except: print("only int numbers"); quit()
  if num < 0 or num>1000: print("Numero demasiado grande. Empieza de nuevo"); quit()
  return num


arr = []
num = input("Ingresa la cantidad de numeros\n:")

try: 
  num = int(num)
except: print("only int numbers"); quit()
if num < 0 or num>50: print("Numero demasiado grande. Empieza de nuevo"); quit()



for i in range(1,num+1): arr.append(val_ai(input(f'Ingresa el numero para la posicion {i}\n:' )))


for i in arr: print(i)
  
    