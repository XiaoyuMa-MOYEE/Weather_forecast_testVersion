import requests

def greet(name):
    return f"你好，{name}"

def testOfData():
    city = "Beijing"

# 发送 GET 请求
    response = requests.get(f'https://wttr.in/{city}?format=%l:+%c+%t+%C+%w')

# 输出响应内容
    print(response.text)
