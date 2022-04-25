

a=[]
for num in range(7, 89+1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           a.append(num)
print('"100000 below 21 sum  of consecutive prime number is"-',sum(a),end='')

           