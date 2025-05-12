import ipywidgets as widgets
from IPython.display import display

# 创建按钮
button = widgets.Button(description="点击我")

# 创建一个标签，用于显示按钮点击后的消息
label = widgets.Label(value="请点击按钮")

# 按钮点击时的回调函数
def on_button_click(b):
    label.value = "按钮已点击!"

# 绑定按钮点击事件
button.on_click(on_button_click)

# 显示按钮和标签
display(button, label)