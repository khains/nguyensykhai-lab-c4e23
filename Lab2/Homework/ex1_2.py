from youtube_dl import YoutubeDL
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")
soup = BeautifulSoup(page_content, "html.parser")
section= soup.find("section", "section chart-grid")
ul = section.find("ul")
li_list = ul.find_all("li")
news_list = []
for li in li_list:
    a = li.h3.a
    b = li.h4.a
    names = a.string
    artists = b.string

    news = OrderedDict({
        "Names": names,
        "Artists": artists,
    })
    news_list.append(news)
    options = {
    'default_search': 'ytsearch',
    'max_downloads': 1 
    }
    dl = YoutubeDL(options)
    dl.download([names])
pyexcel.save_as(records = news_list, dest_file_name = "itunes.xlsx")

