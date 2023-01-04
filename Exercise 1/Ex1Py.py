def val(num, pross):
  try: num = int(num)
  except: print("only int numbers"); quit()
  if pross == 1:
    if num < 0 or num>50: print("Numero demasiado grande. Empieza de nuevo"); quit()
  if pross == 2:
    if num < 0 or num>1000: print("Numero demasiado grande. Empieza de nuevo"); quit()
  return num
#
arr = []
num = val(input("Ingresa la cantidad de numeros\n:"), 1)
#
for i in range(1,num+1): arr.append(val(input(f'Ingresa el numero para la posicion {i}\n:' ),2))
#
for i in arr: print(i)
  
    