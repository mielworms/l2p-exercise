import os
velocity = float(input("Enter a value for speed: "))
frequency = float(input("Enter a value for frequency: "))
input("Press enter to continue.")
os.system('clear')
print("The speed (m/s): ",velocity)
print("The frequency (Hz): ",frequency)
print("The wavelength (m): ",(velocity/frequency))