
name = input("Enter student name: ")

m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
