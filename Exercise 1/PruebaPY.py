def func():
  d = {1:"a", 2.0:"b", 2: "c", 2:"v"}
  return d[2.0]

print(func())



#x= {9,8,5}
#y= {9,5,8}
#print(x == y)
#print(x is y)

# t = [1,2],(1,2)
# t = 1,2
# print(t)
# print(type(t))

#print((lambda a,b:a*b)(5,4)- True)



# my_list = [x for x in range(10) if x%2]

# print(my_list)

# import random
# # numbers = [];
# count = input ("HOW MANY NUMBERS YOU WANT TO CALCULATE GCD?\n")
# count = int(count)
# # for i in range(0, int(count)):
# #   number = int(input("ENTER THE NUMBER : \n")) 
# #   numbers.append(number)

# random_numbers = [random.randint(1, 100) for x in range(count)]
  
# numbers_sorted = sorted(random_numbers)
# print  ('NUMBERS SORTED IN INCREASING ORDER\n',numbers_sorted)
# gcd = numbers_sorted[0]

# for i in range(1, int(count) ):
#   print("For:")
#   divisor = gcd
#   print("divisor:", divisor)
#   print("gcd:", gcd)
#   dividend = numbers_sorted[i]
#   print("dividend:", numbers_sorted[i])
#   remainder = dividend % divisor
#   print("remainder:", remainder)
#   if remainder == 0 :
#     print("IF***")
#     gcd = divisor
#   else :
#     print("Else***")
#     #while not remainder == 0 :
#     while remainder != 0: 
#       print("while****", remainder, divisor)
#       dividend_one = divisor
#       print("dividend_one:", dividend_one)
#       divisor_one = remainder
#       print("divisor_one:", divisor_one)
#       remainder = dividend_one % divisor_one
#       print("remainder:", remainder)
#       gcd = divisor_one
#       print("gcd:", gcd)
#       print("End while****")

# print(gcd)

