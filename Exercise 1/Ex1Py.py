def val(num, pross, msg = "Number too large. Start over"):
  try: num = int(num)
  except: print("only int numbers"); quit()
  if pross == 1 and (num < 0 or num>50): print(msg); quit()
  if pross == 2 and (num < 0 or num>10**3): print(msg); quit()
  return num  
#
arr = []

num = val(input("Enter the amount of numbers\n:"), 1)
#
for i in range(1,num+1): arr.append(val(input(f'Enter the number for {i} position \n:' ),2))
#
for i in arr: print(i)