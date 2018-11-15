from random import *
from func_intro import eval
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 10)
    y = randint(0, 10)
    error = randint(-1, 1)
    op_list = ["+", "-", "*", "/"]
    o = choice(op_list)
    s = eval(x, y, o)
    r = s + error 
    return [x, y, o, r]
a, b, op, r = generate_quiz()
print(a, op ,b ,"=", r)
def check_answer(x, y, op, result, user_choice):
    
