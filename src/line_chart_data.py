from get_weather_data import get_weather_forecast
from natural_language_responses import get_weather_response


def get_line_chart_data(questions, city, max_day): #传入参数
    result,data = get_weather_forecast(city, max_day) #获得参数
    answer = get_weather_response(questions) #获得参数


    def handle_pop():
        print("处理带伞相关问题。")

    def handle_describe():
        print("处理天气描述相关问题。")

    def handle_cloth():
        print("处理穿衣建议相关问题。")

    def handle_temperature():
        print("处理温度相关问题。")

    def handle_wind():
        print("处理风速相关问题。")

    def handle_humidity():
        print("处理湿度相关问题。")

    # 输入处理函数返回类型并根据返回值执行不同操作
    def process_answer(answer):
        # 根据返回的类型标识符执行不同的函数
        if answer == "pop":
            handle_pop()
        elif answer == "describe":
            handle_describe()
        elif answer == "cloth":
            handle_cloth()
        elif answer == "temperature":
            handle_temperature()
        elif answer == "wind":
            handle_wind()
        elif answer == "humidity":
            handle_humidity()
        else:
            print("无法识别的答案。")
    process_answer(answer)