from aip import AipSpeech
from aip import AipNlp
from uuid import uuid4
import os
import tuling123

APP_ID = '14947852'
API_KEY = 'vYMzzbgurIl8xj3aklia9zZ8'
SECRET_KEY = '0MgFAOVGG6rL2OgoLifyT2TFEydV0RoW'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
client_nlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def audio2text(filename):
    os.system(f"ffmpeg -y  -i {filename} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filename}.pcm")
    with open(f"{filename}.pcm", 'rb') as fp:
        res = client.asr(fp.read(), 'pcm', 16000, {'dev_pid': 1536, })
        print(res.get("result")[0])
        return res.get("result")[0]


def text2audio(text):
    filename = uuid4()
    result = client.synthesis(text, 'zh', 1, {"spd": 4, 'vol': 5, "pit": 8, "per": 4})
    if not isinstance(result, dict):
        with open(f'{filename}.mp3', 'wb') as f:
            f.write(result)

    return f'{filename}.mp3'


def my_nlp(text):
    if client_nlp.simnet("你叫什么名字", text).get("score") >= 0.7:
        return text2audio("我的名字叫大王八")

    if client_nlp.simnet("你今年多大了", text).get("score") >= 0.7:
        return text2audio("我今年9岁了")

    else:
        return text2audio(tuling123.goto_tuling(text, "Lance"))
