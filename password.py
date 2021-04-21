
import re
def is_valid_password(password):
  if len(password) >= 10 and (password.isalnum() == True) and  re.search("[A-Z]",password):
      return "password accpeted"
  else:
    return ("\nA password must have at least ten characters. "
              "\nA password consists of only letters and digits. "
              "\nA password must contain at least a capital letter in it.")


print(is_valid_password(input("enter your password \n")))



