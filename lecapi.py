import requests
import time
from bs4 import BeautifulSoup
import re
import random
from bot_send_content import bot_say
from tinydb import TinyDB, Query
from lec import get_session_id

db = TinyDB('myproject.json')

def check(s):
    pattern = r'^<script\b[^>]*>.*?</script>$'
    return bool(re.match(pattern, s, re.DOTALL))


def get_data(session_node_id):

    url1 = "http://sjcx.buct.edu.cn/practiceext/practiceextAction/project.action"
    url2 = "http://sjcx.buct.edu.cn/aexp/stuLeft.jsp"
    url = 'http://sjcx.buct.edu.cn/practiceext/practiceextAction/practiceext/practiceextAction/choise.action'
    url = 'http://sjcx.buct.edu.cn/practiceext/practiceextAction/practiceext/practiceextAction/myproject.action'
    # url = "http://sjcx.buct.edu.cn/practiceext/practiceextAction/practiceext/practiceextAction/mycredit.action"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': f'route=1efa69ec5b8aa50bb212e6a57af10eb5; JSESSIONID={session_node_id}.node1; aexpsid={session_node_id}.node1',
        'Host': 'sjcx.buct.edu.cn',
        'Referer': 'http://sjcx.buct.edu.cn/practiceext/practiceextAction/project.action',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    response_ = requests.get(url, headers=headers)#,proxies=Proxy)
    return response_


Session_id = get_session_id()
print("Session_id = ", Session_id)
while True:
    xxx = random.randint(1, 3000)
    if xxx < 10:
        print(f"xxx={xxx},Session_id失效")
        bot_say()
        Session_id = "11111"
    response = get_data(Session_id)
    html_code = response.text.strip()
    while check(html_code):
        Session_id = get_session_id()
        response = get_data(Session_id)
        html_code = response.text.strip()
    soup = BeautifulSoup(html_code, 'html.parser')

    rows = soup.find_all('tr')
    data = []
    for row in rows:
        cells = row.find_all('td')
        data.append([cell.text.strip() for cell in cells])
    print("xxx=", xxx, data)
    new_data = []
    for row in data:
        if row:
            lec_keys = ["name", "patch", "begin_time", "end_time", "teacher", "qr_code", "operate"]
            data_dict = dict(zip(lec_keys, row))
            new_data.append(data_dict)
    Lecture = Query()
    for entry in new_data:
        # 新增逻辑
        # db.insert(entry)
        # 更新逻辑
        db.update(entry, Lecture.name == entry["operate"])

    time.sleep(2)

