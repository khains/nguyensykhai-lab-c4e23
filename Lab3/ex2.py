a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = input("Operation(+,-,*,/):")
x1 = a + b
x2 = a - b
x3 = a * b
x4 = a / b
if c == "+" :
    print("a + b = ",x1)
elif c == "-" :
    print("a - b = ",x2)
elif c == "*" :
    print("a * b = ",x3)
elif c == "/":
    print("a / b = ", x4)
else:
    print("Unsupported Operation!")