#Andrew Parker
#10/23/17
#warmup11.py - determine if a number is prime

def isPrime(n):
    for i in range(2, n-1): 
        if n%i == 0:
            return False  
    return True

print(isPrime(6))



"""
def isPrime(n):
    for i in range(2, n-1): 
        if n%i == 0:
            return False  
    else:
        return True
    i = i + 1

print(isPrime(6))"""



  