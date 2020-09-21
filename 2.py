import os
student1 = int(input("Enter the first student's exam score: "))
student2 = int(input("Enter the second student's exam score: "))
student3 = int(input("Enter the third student's exam score: "))
input("Press enter to continue.")
os.system('clear')

print("Student scores:")
list = [student1, student2, student3]
for i in list:
  print (i) 
print("Average: ",(student1 + student2 + student3)/3) 