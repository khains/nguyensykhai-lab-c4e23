from random import randint, choice
from func_intro import eval

def generate_quiz():
    x = randint(0, 10)
    y = randint(0, 10)
    error = randint(-1, 1)
    op_list = ["+", "-", "*", "/"]
    o = choice(op_list)
    s = eval(x, y, o)
    r = s + error 

    return x, y, o, r, error
a, b, op, r, error = generate_quiz()
print(a, op ,b ,"=", r)
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
