import re

# 定义处理函数
def handle_umbrella():
    return "今天有降雨，建议带伞。"

def handle_weather():
    return "今天的天气是晴天。"

def handle_clothing():
    return "今天温暖，建议穿轻便衣物。"

# 问题和响应的映射字典
response_mapping = {
    "Umbrella": handle_umbrella,
    "天气": handle_weather,
    "衣服": handle_clothing
}

# 输入处理函数
def get_weather_response(question):
    # 遍历字典进行关键词匹配
    for keyword, handler in response_mapping.items():
        # re.IGNORECASE 忽略大小写，s?表示匹配单复数
        if re.search(r"\b" + re.escape(keyword) + r"s?\b", question, re.IGNORECASE):
            return handler()
    return "抱歉，我无法理解您的问题。"
print(get_weather_response("Do I need to take an umbrella"))