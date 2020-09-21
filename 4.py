
pi = 3.14 
pie_diameter = 55.4
pie_radius = float(pie_diameter)/2
circumference = 2*float(pi)*float(pie_radius)
print("Jimmy's pie has a circumference of",circumference)

ALTERNATIVE

import os
pi = 3.14 
pie_diameter = float(input("Enter pie diameter: "))
input("Press enter to continue.")
os.system('clear')
pie_radius = float(pie_diameter)/2
circumference = 2*float(pi)*float(pie_radius)
print("Jimmy's pie has a circumference of",circumference)