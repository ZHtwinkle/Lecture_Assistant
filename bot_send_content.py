import requests

import config

bot_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={config.WECOM_KEY}"
headers = {'Content-Type': 'application/json; charset=UTF-8'}


def bot_say():
    json = {

        "msgtype": "text",

        "text": {

            "content": "讲座信息已更新\n具体请前往实践平台查看\n",
            "mentioned_mobile_list": ["@all"]
        }

    }
    requests.post(url=bot_url, json=json, headers=headers)
