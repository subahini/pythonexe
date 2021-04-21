def fibonacci(args):
    a = 0
    b = 1
    d = 0
    c = 0
    if args != 0 :
        while d < args:
            a = b
            b = c
            d = d+1
            c = a + b
    return (c)




print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(3))  # 2
print(fibonacci(7))  # 13
print(fibonacci(12)) # 144


'''bonus work'''
import sys
''' this is  command line argument output'''

def fibonacci_args():
     n =len(sys.argv)-1
     a = 0
     b = 1
     d = 0
     c = 0
     if n > 1:
         while d < n:
             for  d in sys.argv:
              a = b
              b = c
              d = d + 1
              c = a + b
         n = n - 1
     print (c)
     #else :
     #print('ples command line nckndn')


fibonacci_args()