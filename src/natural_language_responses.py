import re


# 定义处理函数
def res_pop():
    return "pop"


def res_describe_weather():
    return "describe"


def res_clothing():
    return "temperature"


def res_temperature():
    return "temperature"


def res_wind():
    return "wind"


def res_humidity():
    return "humidity"


# 问题和响应的映射字典
response_mapping = {
    "umbrella": res_pop,
    "rain": res_pop,
    "precipitation": res_pop,
    "wet": res_pop,
    "showers": res_pop,
    "rainy": res_pop,
    "storms": res_pop,
    "need an umbrella": res_pop,

    "weather": res_describe_weather,
    "forecast": res_describe_weather,
    "today's weather": res_describe_weather,
    "how's the weather": res_describe_weather,
    "what's the weather like": res_describe_weather,

    "clothing": res_clothing,
    "dress": res_clothing,
    "wear": res_clothing,
    "what to wear": res_clothing,
    "should I wear": res_clothing,
    "clothes": res_clothing,

    "temperature": res_temperature,
    "how hot": res_temperature,
    "how cold": res_temperature,
    "hot": res_temperature,
    "cold": res_temperature,
    "temperature today": res_temperature,

    "wind": res_wind,  # 风速
    "wind speed": res_wind,  # 风速
    "how windy": res_wind,  # 风大吗
    "windy": res_wind,  # 风

    "humidity": res_humidity,  # 湿度
    "how humid": res_humidity,  # 湿吗
    "humid": res_humidity  # 湿度
}


# 输入处理函数
def get_weather_response(question):
    # 遍历字典进行关键词匹配
    for keyword, handler in response_mapping.items():
        # re.IGNORECASE 忽略大小写，s?表示匹配单复数
        if re.search(r"\b" + re.escape(keyword) + r"s?\b", question, re.IGNORECASE):
            return handler()
    return "抱歉，我无法理解您的问题。"
# 断点测试
# print(get_weather_response("perth"))
