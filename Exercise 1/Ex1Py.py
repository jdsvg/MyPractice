def val(num, pross, msg = "Number too large. Start over"):
  try: num = int(num)
  except: print("only int numbers"); quit()
  if pross == 1 and (num < 0 or num>50): print(msg); quit()
  if pross == 2 and (num < 0 or num>10**3): print(msg); quit()
  return num  
#
arr = []
c = 0
count = 0
# No Test
# num = val(input("Enter the amount of numbers\n:"), 1)
# No Test
# for i in range(1,num+1): arr.append(val(input(f'Enter the number for {i} position \n:' ),2))

# Test
arr=[8,12,16,24]
# shorted arr
for i in range(0,len(arr)):
  for j in range(i+1,len(arr)):
    if(arr[i]<arr[j]):aux= arr[i];arr[i]=arr[j];arr[j]=aux
#

count = len(arr)
  
numbers_sorted = arr
print  ('NUMBERS SORTED IN INCREASING ORDER\n',numbers_sorted)
gcd = numbers_sorted[0]

for i in range(1, int(count) ):
  divisor = gcd;dividend = numbers_sorted[i];remainder = dividend % divisor
  if remainder == 0 :gcd = divisor
  else :
    while remainder != 0: dividend_one = divisor;divisor_one = remainder;remainder = dividend_one % divisor_one;gcd = divisor_one
      
  
print(gcd)

# ....
# product of the whole list: fP(arr)
# fP(arr)^GCD

print(c)


    
    