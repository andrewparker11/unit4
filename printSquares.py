#Andrew Parker
#10/26/17
#printSquares.py - prints squares 

"""
def squares(rows, cols):
    print('+ - - '*rows+'+')
    print('|     '*cols+'|')
    print('+ - - '*rows+'+')
   
   
squares(5,5)"""



def squares(rows, cols):
    i = 1
    while i<=cols and i<rows:
        print('+ - - '*rows+'+')
        print('|     '*cols+'|')
        i = i+1

squares(8,8)

