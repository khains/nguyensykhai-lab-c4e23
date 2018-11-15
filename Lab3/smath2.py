from random import randint, choice
op_list = ["+", "-", "*", "/"]
c = choice(op_list)
a = randint(0, 10)
b = randint(0, 10)
error = randint(-1, 1)
r1 = a + b + error 
r2 = a - b + error
r3 = a * b + error
r4 = a / b + error
if c == "+" :
    print(a, "+" ,b ,"=", r1)
elif c == "-" :
    print(a, "-" ,b ,"=", r2)
elif c == "*" :
    print(a, "*" ,b ,"=", r3)
elif c == "/":
    if b == 0:
        print("Null")
    else:
        print(a, "/" ,b ,"=", r4)
t = input("Y/N:").upper()
if error == 0 :
    if t == "Y":
        print("Dung")
    else:
        print("Sai")

elif error != 0 :
    if t == "Y":
        print("Sai")
    else:
        print("Dung")
