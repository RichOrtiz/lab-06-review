import sys # coding: utf-8

print ("Here's this BMI calculator thing")

weight = input("Enter your weight(in pounds): ")
height = input("Enter your height(in inches): ")
bmi = 703 * float(weight) / (float(height) * float(height))
roundedbmi = round(bmi,2)
print("Your body mass index (BMI) is: " + str(roundedbmi) + "%")