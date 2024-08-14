from DrissionPage import ChromiumPage, ChromiumOptions
import base64
from PIL import Image
from io import BytesIO
from bd_api import get_code
import time
import config

# pat=r"Chro\Application\chrome.exe"
# co=ChromiumOptions().set_browser_path()# pat)
def get_session_id():
    page = ChromiumPage()  # co)

    flag = True

    while flag:
    # for i in range(1):
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

            ##        ele_juese.page.ele("@value=2")
            ##        ele_juese.click()
            ele_submit = page.ele("@type=submit")
            ele_submit.click()


            time.sleep(2)



            flag = page.handle_alert(timeout=0.5)
            print("验证码正确" if not flag else "验证码错误")


                # if i["name"]=="username":
                #    Flag=False
            # ele=page('实践创新学分')
            # ele_check=ele.ele('@text()=实践创新学分')
            ele_title = page.ele('xpath:/html/body/dl/dd[7]/div')
            ele_title.click()
            # ele_title = page.ele("""text:实践创新活动""")
            # ele_title.click()

            # ele_title = page.ele("""text:我的活动(讲座)""")
            # ele_title.click()

            # page.get("http://sjcx.buct.edu.cn/practiceext/practiceextAction/project.action")
            # print(ele_check)
            # print(page.html)
            # page.get("http://sjcx.buct.edu.cn/aexp/stuLeft.jsp")
            # page.get("http://sjcx.buct.edu.cn/practiceext/practiceextAction/project.action")

            for i in page.cookies(as_dict=False):
                # print(i)
                if i.get("name", 0) == "aexpsid":
                    return i["value"].split(".")[0]
        except Exception as E:
            print(E)
            continue