def spell(txt):
    """Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.
"""
    i =len(txt)-1
    
    while i >= 0:
        print (txt[i])
        i -= 1 
txt = input()
spell(txt)
