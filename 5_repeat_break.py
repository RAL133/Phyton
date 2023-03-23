#
#calculator
#

#1. input
while True:
    x1 = input("Enter x1: ")
    x2 = input("Enter X2: ")
    op = input("Enter Operator: ")
    #2. Process
    if op == "+":
        sum = int(x1) + int (x2)
    elif op == "-":
        sum = int(x1) - int (x2)
    elif op == "*":
        sum = int(x1) * int (x2)
    elif op == "/":
        sum = int(x1) / int (x2)
    elif op == "%":
        sum = int(x1) / int (x2) *100 
    elif op == "Average":
        sum = (int(x1) +int (x2))/2
    #3. output
    print (f"sum: {sum}")
    res = input("Continue? (Y/N)")
    if res.upper()[0] == "N":
        break