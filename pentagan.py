def get_pentagonal_number(n):
    if n > 0:
        for a in range(1,n):
         b = ((3 *(a ** 2)) - a)/2
         print(int(b))
get_pentagonal_number(50)