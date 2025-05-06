import ipywidgets as widgets
from IPython.display import display

# 创建一个整数滑块
slider = widgets.IntSlider(value=10, min=0, max=100)

# 创建一个文本显示器
text = widgets.IntText()

# 把两个组件绑定在一起
widgets.jslink((slider, 'value'), (text, 'value'))

# 显示组件
display(slider, text)
'''
用于数据可视化
'''