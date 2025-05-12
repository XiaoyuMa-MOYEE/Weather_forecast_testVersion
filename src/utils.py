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

#获取天气数据（返回JSON数据）
def get_weather_forecast(city,max_day):
    """
    每个函数需要包含一个文档描述，其中包含函数说明，输入和输出示例
    :param city:城市名称
    :param max_day:1-5的正整数
    """
    #api's key
    api_key = "56d26083c4e5d4828784871da1b7b0b3"
    #api
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "zh_cn"
        #todo:修改语言
    }
    try:
        response = requests.get(url, params=params)
        #若无响应则抛出异常
        response.raise_for_status()
        data = response.json()
        #尝试输出
        # print(data)

        if response.status_code != 200:
            print("请求失败:", data.get("message", "未知错误"))
            return None

        # 按天整理每3小时的天气数据
        forecast_by_day = defaultdict(list)
        for item in data["list"]:
            #日期
            date = item["dt_txt"].split(" ")[0]
            #温度
            temp = item["main"]["temp"]
            #描述
            desc = item["weather"][0]["description"]
            #风速
            speed = item["wind"]["speed"]
            #湿度
            humidity = item["main"]["humidity"]
            time = item["dt_txt"]
            forecast_by_day[date].append((time, temp, desc,speed,humidity))


        # 输出每日天气（优先取 12:00 的数据）
        # print(f"城市：{data['city']['name']}")
        result = {
            "city": data["city"]["name"],
            "forecast": []
        }
        for date, items in list(forecast_by_day.items())[:max_day]:  # 最多5天
            # 选取12:00或默认第一条
            mid = next((x for x in items if "12:00" in x[0]), items[0])
            # print(f"日期：{date},天气情况：{mid[2]},气温：{mid[1]}°C,风速:{mid[3]}, 湿度:{mid[4]}")

            result["forecast"].append({
                "date": date,
                "time": mid[0],
                "temperature": mid[1],
                "description": mid[2],
                "speed": mid[3],
                "humidity": mid[4]

            })
        return result
    except requests.exceptions.RequestException as e:  # 捕获所有requests相关的异常
        print(f"网络请求失败：请检查网络链接\n{e}")
        return None
    #返回失败的返回值
