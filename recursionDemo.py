#Andrew Parker
#10/26/17
#recursionDemo.py - a recursive version of the countdown function

def countdown(n):
    if n == 0:
        print('BOOM!')
    else:
        print(n)
        countdown(n-1)
countdown(5)