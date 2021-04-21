try:
    name = input("enter your name to creat account ")
    #your
    if len(name)<4:
        raise valueError
    else :
        print("Account Created")
except:
    print("Invalid Name")
