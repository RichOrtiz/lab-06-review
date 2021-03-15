tempc = input("Give me the current temperature in celsius: ")
# print(tempc)
# print(type(tempc))
tempf = float(tempc) * 1.8 + 32
roundedtempf = round(tempf,2)
print("The temperature is " + str(roundedtempf) + "°F")
# print(type(tempf))
# tempf = 9 / 5 * tempc + 32
# print(tempc + " degrees celsius is " + tempf + " degrees fahrenheit")

