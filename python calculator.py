firstnum = 0
secnum = 0
operator = ""

firstnum = float(input("Write number "))
secnum = float(input("Write number "))
operator = input("write your operator")

if operator == "*":
    print(str(firstnum * secnum))
elif operator == "+":
    print(str(firstnum + secnum))
elif operator == "-":
    print(str(firstnum - secnum))
elif operator == "/":
    if secnum != 0:
        print(str(firstnum / secnum))
    else:
        print("the second number cannot be 0")
else:
    print("error")


# % module
#   11 % 2 = 2

# take 2 numbers from the user, and print if the list number can be evenly divided by the secnumber
