tempincelsius = input("Please enter a temperature in Celsius... ")
tempincelsius = float(tempincelsius)
# tempincelsius = float(input("Please enter a temperature in Celsius")) <- Alternate solution
# print(type(tempincelsius))
tempinfahrenheit = tempincelsius * 1.8 + 32
tempinfahrenheit = round(tempinfahrenheit, 2)
    # round() is a FUNCTION used to limit the number of decimal places
print(str(tempincelsius) + " degrees Celsius is " + str(tempinfahrenheit) + " degrees Fahrenheit")
