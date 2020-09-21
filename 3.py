import os
class1 = int(input("Number of students in class 1: "))
groups1 = int(input("Number of groups in class 1: "))
print("")
class2 = int(input("Number of students in class 2: "))
groups2 = int(input("Number of groups in class 2: "))
print("")
class3 = int(input("Number of students in class 3: "))
groups3 = int(input("Number of groups in class 3: "))
os.system('clear')

each_grp1, leftover1 = divmod (class1, groups1)
each_grp2, leftover2 = divmod (class2, groups2)
each_grp3, leftover3 = divmod (class3, groups3)

print("Number of students in each group:")
print("Class 1:", each_grp1)
print("Class 2:", each_grp2)
print("Class 3:", each_grp3)
print("Number of students leftover:")
print("Class 1:", leftover1)
print("Class 2:", leftover2)
print("Class 3:", leftover3)

'''
list_eachgrp = [["Class 1:",each_grp1],["Class 2:",each_grp2],["Class 3:",each_grp3]
list_leftover = [["Class 1:",leftover1]["Class 2:",leftover2],["Class 3:",leftover3]
'''