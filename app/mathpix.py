import os
import requests
import base64
import PIL
import json

from io import BytesIO

env = os.environ

credentials_file_name = env.get("MATHPIX_CREDENTIALS")
credentials_file = open(credentials_file_name)
default_headers = json.load(credentials_file)
default_headers["Content-type"] = "application/json"

endpoint = 'https://api.mathpix.com/v3/latex'

def image_uri(pil_image_object):
    buffered = BytesIO()
    pil_image_object.save(buffered, format="JPEG")
    return "data:image/jpg;base64," + base64.b64encode(buffered.getvalue()).decode()

def latex(args, headers=default_headers, timeout=30):
    r = requests.post(endpoint,
        data=json.dumps(args), headers=headers, timeout=timeout)
    return json.loads(r.text)

def convert(image_object):
    fields = {
            "src": image_uri(image_object),
            "ocr": ["math", "text"],
            "formats": ["latex_styled"]
            }
    return latex(fields)
