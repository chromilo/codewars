# Author: Chromilo Amin
# Email: chromilo.amin@gatech.edu
# Date: Dec 18, 2020
#Kata: Implement a difference function, which subtracts one list from another and returns the result.It should remove all values from list a, which are present in list b. 
# array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a,b):
   c = []
   if(len(a)==0):
      return(c)
   for u in a:
      found=False
      for v in b:
         if(u==v):
            found=True
      if(found==False):
         c.append(u)
   return(c)

print(array_diff([1,2],[1]))

