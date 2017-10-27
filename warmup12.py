#Andrew Parker
#10/27/17
#warmup12.py - finds GCF

def GCF(n1,n2):
    for i in range(n1,0,-1): 
        if n1%i == 0 and n2%i == 0:
            return(i)

print(GCF(21,28))