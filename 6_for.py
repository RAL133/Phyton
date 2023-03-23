#1. input
x1 = input("Enter X1: ")
x2 = input("Enter X2: ")
#2. Process
sum=0
for x in range (int(x1), int(x2)+1):
    sum += x
#3. output
print(f"sum:{sum}")
