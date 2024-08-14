import requests

bot_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6e39100a-d905-4950-90fa-bdd035565197"
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

