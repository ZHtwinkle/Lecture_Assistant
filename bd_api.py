import requests
import base64


def get_code(image_path):

    url = "ocr地址"
    headers = {'Content-type': 'application/json'}
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    data = {
        "image_base64": encoded_string
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()["result"]

# example
# print(get_code("output_image.png"))
