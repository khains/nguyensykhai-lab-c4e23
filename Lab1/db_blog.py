from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds147440.mlab.com:47440/c4e23-blog"
#1 Connect
client = MongoClient(uri)
#2 Get default database
db = client.get_database()
#3 Get collection
posts = db["posts"]
movies = db["movies"]
#4 Create data
new_post = {
    "title": "Hom nay troi nang",
    "content": "Toi o nha code",
}
new_movie = {
    "title":"Batman begins",
    "ratting": 8.0
}
#5.1 Insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

#5.2 Read data
post_list = posts.find()
# p = post_list[1]
for p in post_list:
    print(p["title"])
    print(p["content"])
    print("%%%%%%%%%%%%%%%%%%%%")
#6 Close connection
client.close()