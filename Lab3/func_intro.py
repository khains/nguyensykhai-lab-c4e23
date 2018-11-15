# def add(a, b):
#     r = a + b
#     return r
# # call function
# s = add(7, 8)
# print(s)
# from random import randint, choice
# op_list = ["+", "-", "*", "/"]
# op = choice(op_list)
# a = randint(0, 10)
# b = randint(0, 1)
# error = randint(-1, 1)
# r1 = a + b + error 
# r2 = a - b + error
# r3 = a * b + error
# r4 = a / b + error
def eval(a, b, op):
    if op == "+":
        r = a + b
        return r
    elif op == "-":
        r = a - b
        return r
    elif op == "*":
        r = a * b
        return r
    elif op == "/":
        if b == 0:
            print("Null")
        else:
            r = a / b
            return r
    else:
        print("Unsupported Operation!")
    
# s = eval(9, 10, "*")
# print(s)
