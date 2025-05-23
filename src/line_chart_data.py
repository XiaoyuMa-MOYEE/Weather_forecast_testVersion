from get_weather_data import get_weather_forecast
from natural_language_responses import get_weather_response


def get_line_chart_data(questions, city, max_day):  # 传入参数

    result, forecast_by_day = get_weather_forecast(city, max_day)  # 获得参数
    answer = get_weather_response(questions)  # 获得参数

    def handle_pop():
        precipitation_list = []
        for date, items in forecast_by_day.items():
            for item in items:
                time = item[0]
                pop = item[5]
                precipitation_list.append((time, pop))
        return precipitation_list

        # print("处理带伞相关问题。")

    def handle_describe():
        precipitation_list = []
        for date, items in forecast_by_day.items():
            for item in items:
                time = item[0]
                weather = item[2]
                precipitation_list.append((time, weather))
        return precipitation_list
        # print("处理天气描述相关问题。")

    def handle_cloth():
        precipitation_list = []
        for date, items in forecast_by_day.items():
            for item in items:
                time = item[0]
                temperature = item[1]
                precipitation_list.append((time, temperature))
        return precipitation_list
        # print("处理穿衣建议相关问题。")

    def handle_temperature():
        precipitation_list = []
        for date, items in forecast_by_day.items():
            for item in items:
                time = item[0]
                temperature = item[1]
                precipitation_list.append((time, temperature))
        return precipitation_list
        # print("处理温度相关问题。")

    def handle_wind():
        precipitation_list = []
        for date, items in forecast_by_day.items():
            for item in items:
                time = item[0]
                wind = item[3]
                precipitation_list.append((time, wind))
        return precipitation_list
        # print("处理风速相关问题。")

    def handle_humidity():
        precipitation_list = []
        for date, items in forecast_by_day.items():
            for item in items:
                time = item[0]
                humidity = item[4]
                precipitation_list.append((time, humidity))
        return precipitation_list
        # print("处理湿度相关问题。")

    def process_answer(answer):
        if answer == "pop":
            index = 1
            return handle_pop(),index,answer
        elif answer == "describe":
            index = 1
            return handle_describe(),index,answer
        elif answer == "cloth":
            index = 1
            return handle_cloth(),index,answer
        elif answer == "temperature":
            index = 1
            return handle_temperature(),index,answer
        elif answer == "wind":
            index = 1
            return handle_wind(),index,answer
        elif answer == "humidity":
            index = 1
            return handle_humidity(),index,answer
        else:
            index = 0
            lines = ["您的问题有些模糊。给您提供全部数据的简单描述，如需折线图，请具体询问：如“天气怎么样，是否会降水”"]
            for day in result['forecast']:
                lines.append(
                    f"日期：{day['date']},天气情况：{day['description']},气温：{day['temperature']}°C,"
                    f"风速:{day['speed']}, 湿度:{day['humidity']},降水率:{day['pop']}"
                )
            answer = "null"
            return lines, index,answer

    return process_answer(answer)  # 关键补充：外层返回结果



