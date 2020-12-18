# Author: Chromilo Amin
# Email: chromilo.amin@gatech.edu
# Date: Dec 18, 2020
# Kata: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them) Courtesy of projecteuler.net 

def sum_of_multiples(number):
   if(number<0):
      return(0)
   lst = []
   for i in range(3,number):
      if((i % 3)==0):
         print(i)
         lst.append(i)	 
	 
   for i in range(5,number):
      if((i % 5)==0):
         try:
            lst.index(i)
         except ValueError:
            lst.append(i)
            print(i)	
   sum=0
   for i in lst:
      sum += i
   return(sum)

print(sum_of_multiples(10))

