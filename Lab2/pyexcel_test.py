import pyexcel
from collections import OrderedDict

#2 Prepare data
x_list = [
    OrderedDict({
        "name": "1",
        "age": 1,
    }),
    OrderedDict({
       "name": "2",
        "age": 2, 
    }),
    OrderedDict({
        "name": "3",
        "age": 3,
    })
]

# List compe
pyexcel.save_as(records = x_list, dest_file_name = "x_list.xls")