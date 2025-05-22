# 天气预报项目概述

本项目使用 **Python** 语言，在 **Google Colab / Jupyter Notebook** 环境下部署。主要用于接收用户以自然语言方式提出的天气问题，并将查询结果以折线图的形式可视化展示。
请通过运行submit_EN.ipynb运行项目
---

## 📁 项目介绍

项目分为以下几个主要模块：

### 1. 数据获取模块

- 调用 [OpenWeatherMap API](https://openweathermap.org/api)
- 使用 `api-key` 获取天气数据
- 对获取的数据进行解析与结构化处理

### 2. UI 用户交互模块

- 使用 `ipywidgets` 等 Jupyter 图形化插件
- 提供输入框、下拉选择、按钮等控件
- 实现无需命令行操作的图形化交互方式
- 交互方式更直观、灵活

### 3. 折线图生成模块

- 调用数据获取模块返回的数据
- 使用 `Plotly` 等可视化工具
- 将温度、降水率、风速等信息转换为折线图展示

### 4. 自然语言匹配模块

- 基于关键词字典的匹配方法
- 解析用户问题中的关键词，判断提问方向
- 支持独立维护和扩展关键词库（便于修改）

### 5. 其他模块

- 数据处理中间模块：负责格式转换与归类
- 用户输入校验模块：用于检测城市名、天数等参数是否合法

---

## 🚀 使用方式

1. 在 Google Colab 中打开项目 Notebook
2. 点击菜单栏中的 “运行全部”
3. 等待交互式 UI 加载完成
4. 根据提示输入信息并点击按钮进行查询

---

### 🔍 示例操作

> 运行全部  
> 输入：
> - **City**: `perth`
> - **Forecast Days**: `5`
> - **Question**: `Will it rain tomorrow?`

系统将自动分析问题关键词，获取天气数据，并返回折线图展示降雨概率。

---

## 📌 技术栈

- Python 3.x
- OpenWeatherMap API
- ipywidgets
- Plotly
- requests
- Jupyter Notebook / Google Colab

---

## 📎 备注

- 确保在运行前设置好 API 密钥（可通过环境变量 `OPENWEATHER_API_KEY` 设置）
- 网络连接需正常，以调用外部 API 获取数据
## 📎 项目结构

- src文件夹：含有全部的模块化代码和初始ipynb文件
- AI Diagonal文件夹： 包含全部AI对话记录，[cn]开头的文件为原始记录，[EN]开头文件为英文记录
- Project Development Reflection为项目反思文件
- Notebook文件为submit_EN.ipynb
- src文件夹中包含历史文件

