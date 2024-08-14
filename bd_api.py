import base64
import urllib
import requests
import config


API_KEY = config.API_KEY
SECRET_KEY = config.SECRET_KEY

def get_pic_code(pic_path):
    def get_file_content_as_base64(pic_path, urlencoded=True):
        """
        获取文件base64编码
        :param path: 文件路径
        :param urlencoded: 是否对结果进行urlencoded
        :return: base64编码信息
        """
        with open(pic_path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf8")
            if urlencoded:
                content = urllib.parse.quote_plus(content)
        return content
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + get_access_token()
    image=get_file_content_as_base64(pic_path)
    # image 可以通过 get_file_content_as_base64("C:\fakepath\output_image.png",True) 方法获取
    payload=f'image={image}&detect_direction=false&paragraph=false&probability=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    try:
        ans = str(response.json().get("words_result")[0]["words"])

        # print("\n",ans)
        # ans="1234"
        return str(ans)
    except:
        print(response.text)
        return "None"

def get_code():
    def get_file_content_as_base64(path, urlencoded=True):
        """
        获取文件base64编码
        :param path: 文件路径
        :param urlencoded: 是否对结果进行urlencoded
        :return: base64编码信息
        """
        with open(path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf8")
            if urlencoded:
                content = urllib.parse.quote_plus(content)
        return content
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + get_access_token()
    image=get_file_content_as_base64("output_image.png")
    # image 可以通过 get_file_content_as_base64("C:\fakepath\output_image.png",True) 方法获取
    payload=f'image={image}&detect_direction=false&paragraph=false&probability=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    ans = str(response.json().get("words_result")[0]["words"])
    # print(response.text)
    # print("\n",ans)
    # ans="1234"
    return ans

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


