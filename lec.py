import base64
import time
from io import BytesIO

from DrissionPage import ChromiumPage
from PIL import Image

import config
from bd_api import get_code


def get_session_id():
    page = ChromiumPage()
    flag = True
    while flag:
        try:
            page.get('http://sjcx.buct.edu.cn/')
            img = page('@flag=VIMG')
            src = img.src()
            base64_string = base64.b64encode(src).decode()
            image_data = base64.b64decode(base64_string)
            img = Image.open(BytesIO(image_data))
            img.save('output_image.png')
            validate_code = get_code()
            print(validate_code)
            username = config.username
            password = config.password
            ele_username = page.ele("@name=username")
            ele_username.clear()
            ele_username.input(username)
            ele_password = page.ele("@name=password")
            ele_password.clear()
            ele_password.input(password)
            ele_validate_code = page.ele("@name=validateCode")
            ele_validate_code.clear()
            ele_validate_code.input(validate_code)
            ele_juese = page.ele("@name=juese")
            ele_juese.select.by_value(2)
            ele_submit = page.ele("@type=submit")
            ele_submit.click()
            time.sleep(2)
            flag = page.handle_alert(timeout=0.5)
            print("验证码正确" if not flag else "验证码错误")

            ele_title = page.ele('xpath:/html/body/dl/dd[7]/div')
            ele_title.click()
            for i in page.cookies(as_dict=False):
                if i.get("name", 0) == "aexpsid":
                    return i["value"].split(".")[0]
        except Exception as E:
            print(E)
            continue
