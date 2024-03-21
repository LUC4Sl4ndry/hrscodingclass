num = int(input("please enter your base number")) # 3
exp = int(input("please enter your exponent")) # 4
 
# 3 x 3 x 3 x 3
 
temp = num # 3
for _ in range(exp - 1):
    temp = temp * num
 
print(temp)