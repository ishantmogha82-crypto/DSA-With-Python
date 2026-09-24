def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
def sumodd(n):
    if n == 1:
        return 1
    return 2*n-1 + sumodd(n-1)
def sumeven(n):
    if n == 1:
        return 2
    return 2*n + sumeven(n-1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)
def squares(n):
    if n == 0:
        return 0
    return n**2 + squares(n-1)
def digit(n):
     if n == 0:
         return 0
     return (n%10)+digit(n//10)
def sums(n):
    if n == 0:
        return 0
    return 1 + sums(n//10)
def  fab(n):
    if n == 0:
        return 0
    
print("Sum is",sums(234))


        

    
        