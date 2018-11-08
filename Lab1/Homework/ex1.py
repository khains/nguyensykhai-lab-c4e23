from datetime import datetime
from threading import Timer
import random
from gmail import GMail, Message
gmail = GMail("khains0000@gmail.com", "sykhai123")
sickness_list = ["thương hàn", "tiêu chảy", "kiết lị"]
template = '''
<p>Ch&agrave;o sếp,</p>
<p>H&ocirc;m nay em ngủ dậy thấy {{symptom}}, b&aacute;c sĩ bảo em bị {{sick}}.</p>
<p>Sếp cho em nghỉ h&ocirc;m nay nh&eacute;.</p>
<p>Nh&acirc;n vi&ecirc;n của sếp.</p>
'''
sickness = random.choice(sickness_list)
symptom = "đau bụng"
n = template.replace("{{sick}}", sickness).replace("{{symptom}}", symptom)
message = Message("Đơn xin nghỉ làm", to="nskhai3897@gmail.com", html= n)
g = gmail.send(message)
x = datetime.today() 
y = x.replace(hour=19, minute=14, second=0) 
delta_t = y - x
secs=delta_t.seconds+1
t = Timer(secs, g)
t.start()
