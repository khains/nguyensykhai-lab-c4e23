from youtube_dl import YoutubeDL

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

# dl.download ([ ' https://www.youtube.com/watch?v=t7tZFq29lis ' , ' https://www.youtube.com/watch?v=y576-ONm5II ' ])

options = {
    ' format ' : ' bestaudio / audio '  # Cho trình tải xuống chỉ tải xuống chất lượng âm thanh tốt nhất
}
dl = YoutubeDL (options)
dl.download ([ ' https://www.youtube.com/watch?v=c3jHlYsnEe0 ' ])

