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

    "weather": res_describe_weather,  # 天气描述
    "forecast": res_describe_weather,  # 天气预报
    "today's weather": res_describe_weather,  # 今日天气
    "how's the weather": res_describe_weather,  # 如何描述天气
    "what's the weather like": res_describe_weather,  # 天气如何

    "clothing": res_clothing,         # 穿衣建议
    "dress": res_clothing,            # 穿什么衣服
    "wear": res_clothing,             # 穿戴
    "what to wear": res_clothing,     # 穿什么衣服
    "should I wear": res_clothing,    # 我应该穿什么
    "clothes": res_clothing,          # 衣服

    "temperature": res_temperature,   # 温度
    "how hot": res_temperature,       # 多热
    "how cold": res_temperature,      # 多冷
    "temperature today": res_temperature,  # 今天气温

    "wind": res_wind,                 # 风速
    "wind speed": res_wind,           # 风速
    "how windy": res_wind,            # 风大吗
    "windy": res_wind,                # 风

    "humidity": res_humidity,         # 湿度
    "how humid": res_humidity,        # 湿吗
    "humid": res_humidity             # 湿度
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

