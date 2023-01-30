def val(num, pross, msg = "Number too large. Start over"):
  try: num = int(num)
  except: print("only int numbers"); quit()
  if pross == 1 and (num < 0 or num>50): print(msg); quit()
  if pross == 2 and (num < 0 or num>10**3): print(msg); quit()
  return num  
#
def shorted_arr(arr):
  for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
      if(arr[i]<arr[j]):aux= arr[i];arr[i]=arr[j];arr[j]=aux
  return arr
#
def gcd(arr):
  gcd = arr[0]
  for i in range(1, len(arr) ):
    divisor = gcd;dividend = arr[i];remainder = dividend % divisor
    if remainder == 0 :gcd = divisor
    else :
      while remainder != 0: dividend_one = divisor;divisor_one = remainder;remainder = dividend_one % divisor_one;gcd = divisor_one
  return gcd 
  
#
x = 1
arr = []
# num = val(input("Enter the amount of numbers\n:"), 1)
# for i in range(1,num+1): arr.append(val(input(f'Enter the number for {i} position \n:' ),2))
#
# TEST
arr=[2,6,6]
#
arr = shorted_arr(arr);gcd = gcd(arr)
for i in arr: x*=i
print(x**gcd)





    
    