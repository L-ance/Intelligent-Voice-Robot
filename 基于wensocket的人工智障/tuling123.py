import requests

tuling_url = "http://openapi.tuling123.com/openapi/api/v2"
arg = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": "讲个故事"
        }
    },
    "userInfo": {
        "apiKey": "0c6f2261601543fa900e3aa0b1426e19",
        "userId": "lance"
    }
}


def goto_tuling(Q, uid):
    arg["perception"]["inputText"]["text"] = Q
    arg["userInfo"]["userId"] = uid
    res = requests.post(tuling_url, json=arg)
    res_json = res.json()
    print(res)  # <Response [200]>
    print(res.json())
    """
    {
     'intent': {'actionName': '', 'code': 10008, 'intentName': '', 'parameters': {'date': '', 'city': '保定'}}, 
    'results': [{'groupType': 1, 'resultType': 'text', 
     'values': {'text': '保定:周二 11月27日,晴转多云 南风微风,最低气温-3度，最高气温11度'}}]
     }
     """
    print(res_json.get("results")[0]["values"]["text"])
    return res_json.get("results")[0]["values"]["text"]


# goto_tuling('保定天气怎么样', 'lance')
