""" SIMPLE CONVERSIONS"""

# MILES AND KILOMETERS
print(" MILES AND KILOMETERS")
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles *1.61
kilometers_to_miles =kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#  CELSIUS AND FAHRENHEIT
print("CELSIUS AND FAHRENHEIT")
celsius = 26.67
fahrenheit = 80

toCelcius = (fahrenheit -32)*(5 /9)
tofahrenheit = celsius*(9 / 5)+ 32
print( celsius  ," celsius is ",round(tofahrenheit ,2),"farenheit")
print(fahrenheit ,"fahernheit is",round(toCelcius ,3),"celcius")


# USD TO EUR
print("USD TO EURO")
usd =33.50
euro =40

toEuro = usd /0.84
toUsd = euro*0.84

print(usd ,"usd is ",round(toEuro))
print(euro ,"euro is",round(toUsd))
      
