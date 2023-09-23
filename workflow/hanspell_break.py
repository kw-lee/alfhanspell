# -*- coding: utf-8 -*-
"""
Python용 한글 맞춤법 검사 모듈
from https://github.com/ssut/py-hanspell.git
"""


import requests
import json
import time
import sys
import xml.etree.ElementTree as ET
import re
from urllib import parse

from workflow import __version__

base_url = 'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy'

_agent = requests.Session()
PY3 = sys.version_info[0] == 3

def read_token():
    with open("token.txt", "r") as f:
        TOKEN = f.read()
    return TOKEN

def update_token(agent):
    """update passportkey
    from https://gist.github.com/AcrylicShrimp/4c94db38b7d2c4dd2e832a7d53654e42
    """
    
    html = agent.get(url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=맞춤법검사기') 

    match = re.search('passportKey=([a-zA-Z0-9]+)', html.text)
    if match is not None:
        TOKEN = parse.unquote(match.group(1))
        with open("token.txt", "w") as f:
            f.write(TOKEN)
    return TOKEN

def _remove_tags(text):
    text = u"<content>{}</content>".format(text).replace("<br>", "\n")
    # 띄어쓰기 그대로 사용
    if not PY3:
        text = text.encode("utf-8")

    result = "".join(ET.fromstring(text).itertext())

    return result

def _get_data(text, token):
    payload = {
        "q": text,
        "color_blindness": 0,
        "passportKey": token
    }
    headers = {
        "Host": "m.search.naver.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
        "referer": "https://search.naver.com/",
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept": "*/*"
    }
    r = _agent.get(base_url, params=payload, headers=headers)
    data = json.loads(r.text)
    return data

def get_spell_check_data(text):
    TOKEN = read_token()
    data = _get_data(text, TOKEN)
    if "error" in data["message"].keys():
        TOKEN = update_token(_agent)
        data = _get_data(text, TOKEN)
        if "error" in data["message"].keys():
            return "맞춤법 검사가 불가능합니다."
    html = data["message"]["result"]["html"]
    return _remove_tags(html)
