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
num = val(input("Enter the amount of numbers\n:"), 1)
#
for i in range(1,num+1): arr.append(val(input(f'Enter the number for {i} position \n:' ),2))

# Test
# arr=[9,3,6,7]

for i in range(0,len(arr)):
  for j in range(i+1,len(arr)):
    if(arr[i]<arr[j]):aux= arr[i];arr[i]=arr[j];arr[j]=aux
#
for i in range(0, len(arr)):
  for j in range(0,len(arr)):
    if(arr[i]%arr[j]==0 or arr[j]%arr[i]==0):
      count+=1;c=arr[i]
      if(count == len(arr)):break  
      else:c=1
    else:count=0

# ....
# product of the whole list: fP(arr)
# fP(arr)^GCD

print(c)


    
    