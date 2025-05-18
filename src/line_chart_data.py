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
            return handle_pop()
        elif answer == "describe":
            return handle_describe()
        elif answer == "cloth":
            return handle_cloth()
        elif answer == "temperature":
            return handle_temperature()
        elif answer == "wind":
            return handle_wind()
        elif answer == "humidity":
            return handle_humidity()
        else:
            lines = ["您的问题有些模糊。给您提供全部数据的简单描述，如需折线图，请具体询问：如“天气怎么样，是否会降水”"]
            for day in result['forecast']:
                lines.append(
                    f"日期：{day['date']},天气情况：{day['description']},气温：{day['temperature']}°C,"
                    f"风速:{day['speed']}, 湿度:{day['humidity']},降水率:{day['pop']}"
                )
            return "\n".join(lines)

    return process_answer(answer)  # 关键补充：外层返回结果


print(get_line_chart_data("hot", "perth", 5))
