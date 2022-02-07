# The recursive facorial function
def factorial(n):
     if (n < 0):
          return -1
     elif (n==0):
          return 1
     else:
          return n * factorial(n-1)
     
