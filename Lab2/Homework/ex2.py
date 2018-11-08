from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")
soup = BeautifulSoup(page_content, "html.parser")
div = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
table = div.find("table", id ="tableContent")
tr_list = table.find_all("tr")
news_list = []
for t in tr_list:
    td_list= t.find_all("td")
    kq={}
    for i in range(len(td_list)):
        if td_list[i].string != None:
            if i==0:
                kq["Hạng mục"]=td_list[i].string.strip()
            elif i==1:
                kq["Qúy 4-2016"]=td_list[i].string.strip()
            elif i==2:
                kq["Quý 1-2017"]=td_list[i].string.strip()
            elif i==3:
                kq["Quý 2-2017"]=td_list[i].string.strip()
            elif i==4:
               kq["Quý 3-2017"]=td_list[i].string.strip()
    if kq != {}:
        news_list.append(kq)
pyexcel.save_as(records=news_list,dest_file_name="Ketqua.xlsx")