#Andrew Parker
#10/27/17
#warmup12.py - finds GCF

"""
def GCF(n1,n2):
    for i in range(2, n-1): 
        if n%i == 0:
            return False  
    return True

print(GCF(10,15))"""

def GCF(n1,n2):
    for i in range(n1,1,-1): 
        if n1%i == 0 and n2%i == 0:
            print(i)

GCF(10,15))

