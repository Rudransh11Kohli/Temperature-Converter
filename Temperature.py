c = float(input("Enter the temperature in Celcius? "))
print(c)
print(type(c))

f = (9/5 * c) + 32
print("Temperature in fahrenheit is", f)

if(f>=104):
    print("You have a significant fever!")
elif(f<50):
    print("That is too cold... Seek medical attention!")
else:
    print("It's a pleasant temperature.")
