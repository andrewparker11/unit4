#Andrew Parker
#10/23/17
#warmup11.py - determine if a number is prime

def isPrime(n):
    for i in range(2, n-1): 
        i = 1
        if n%i == 0:
            return False  
    else:
        return True
    i = i + 1

print(isPrime())




  