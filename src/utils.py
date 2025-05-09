
#旧的用于获取天气的api代码
'''
## 使用API获得数据的旧代码
# def test_of_data():
#     city = "Perth"
#     # 发送 GET 请求
#     # 标准化格式
#     # response = requests.get(f'https://wttr.in/{city}?3&format=%l:+%c+%t+%C+%w')
#     # %l: 地址
#     # %c: 当前天气图标
#     # %t: 温度
#     # %C：天气描述
#     # %w: 风速
#     # 输出响应内容
#
#     # 访问默认格式
#     response = requests.get(f'https://wttr.in/{city}?format=j1')
#     data = response.json()
#     #输出完整data用于观察数据格式
#     print(data)
#     # 访问未来三天的数据
#     for day in data['weather']:
#         date = day['date']
#         maxtemp = day['maxtempC']
#         mintemp = day['mintempC']
#         description = day['hourly'][4]['weatherDesc'][0]['value']  # 中午的天气
#         print(f"{date}: {description}, {mintemp}°C ~ {maxtemp}°C")
#         print(len(data['weather']))
'''
import requests
from collections import defaultdict

def get_weather_forecast(city):
    api_key = "56d26083c4e5d4828784871da1b7b0b3"  # 🔐 直接写在代码里
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "zh_cn"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        print("请求失败:", data.get("message", "未知错误"))
        return

    # 按天整理每3小时的天气数据
    forecast_by_day = defaultdict(list)
    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        time = item["dt_txt"]
        forecast_by_day[date].append((time, temp, desc))

    # 输出每日天气（优先取 12:00 的数据）
    print(f"城市：{data['city']['name']}\n")
    for date, items in list(forecast_by_day.items())[:5]:  # 最多5天
        # 选取12:00或默认第一条
        mid = next((x for x in items if "12:00" in x[0]), items[0])
        print(f"{date}：{mid[2]}，{mid[1]}°C")

# 调用示例
get_weather_forecast("Beijing")
