from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
cus = db["customers"]
cus_list = cus.find()
count1 = 0
count2 = 0
count3 = 0
for i in cus_list:
    if i["ref"] == "events":
        count1 += 1
    if i["ref"] == "wom":
        count2 += 1
    if i["ref"] == "ads":
        count3 += 1
print("So khach hang evnents:", count1)
print("So khach hang wom:", count2)
print("So khach hang ads:", count3)
from matplotlib import pyplot
x = [count1, count2, count3]
y = ["events", "wom", "ads"]
pyplot.pie(x, labels = y, autopct = "%.1f%%", shadow=True, explode=[0.1, 0.1, 0.1])
pyplot.title("So luong khach hang theo nhom")
pyplot.axis("equal")
pyplot.show()