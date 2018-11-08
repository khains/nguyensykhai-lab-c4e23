from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
posts = db["posts"]
new_post = {
    "title": "Vẽ em bằng màu nỗi nhớ",
    "author": "Nguyễn Sỹ Khải",
    "content":'''Đối với anh, hình ảnh em luôn là người con gái tuyệt vời nhất. 
                 Tuy khái niệm màu sắc đã không còn tồn tại trong anh từ lâu. 
                 Nhưng anh vẫn luôn nhớ tới em bằng một màu sắc đặc biệt. 
                 Anh sẽ vẽ em bằng màu nỗi nhớ.''',
}
posts.insert_one(new_post)
client.close()