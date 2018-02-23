num = int(input("Enter a number: "))
for n in range(10000):
 if (num % 2) == 0:
   print("{0} is Even".format(num))
   break
 else:
   print("{0} is Odd".format(num))
   break
