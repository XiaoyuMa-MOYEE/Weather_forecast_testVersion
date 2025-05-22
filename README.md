# 🌦️ Weather Forecast Project Overview

This project is developed in **Python** and runs in a **Google Colab / Jupyter Notebook** environment. It is designed to allow users to ask weather-related questions in natural language and receive visualized responses in the form of line charts.

Please run the project using `submit_EN.ipynb`.

---

## 📁 Project Introduction

The project is divided into the following main modules:

### 1. Data Retrieval Module

- Calls the [OpenWeatherMap API](https://openweathermap.org/api)
- Uses an `API key` to access weather data
- Parses and structures the retrieved data for further use

### 2. UI Interaction Module

- Uses `ipywidgets` and other Jupyter visualization plugins
- Provides input fields, dropdown menus, buttons, etc.
- Enables intuitive, graphical interaction without command-line input
- Offers a flexible and user-friendly interface

### 3. Line Chart Generation Module

- Processes data retrieved from the data module
- Utilizes tools like `Plotly` for visualization
- Displays temperature, precipitation probability, wind speed, etc., in dynamic line charts

### 4. Natural Language Matching Module

- Implements keyword-based dictionary matching
- Extracts key terms from user questions to determine the query intent
- Designed for modular maintenance and easy expansion of the keyword set

### 5. Additional Modules

- **Data Formatting Module**: Handles intermediate data structuring and conversion
- **Input Validation Module**: Verifies the validity of user input (e.g., city name, forecast days)

---

## 🚀 How to Use

1. Open the notebook in Google Colab
2. Click “Run All” from the top menu
3. Wait for the interactive UI to load
4. Follow the prompts to input your question and submit your query

---

### 🔍 Example Usage

> Click “Run All”  
> Input:
> - **City**: `perth`
> - **Forecast Days**: `5`
> - **Question**: `Will it rain tomorrow?`

The system will automatically detect relevant keywords, fetch forecast data, and generate a line chart showing the probability of rainfall.

---

## 📌 Tech Stack

- Python 3.x
- OpenWeatherMap API
- ipywidgets
- Plotly
- requests
- Jupyter Notebook / Google Colab

---

## 📎 Notes

- Ensure the API key is properly configured before running (recommended via the `OPENWEATHER_API_KEY` environment variable)
- A stable internet connection is required to fetch external API data

---

## 📎 Project Structure

- `src` folder: Contains all modular code and initial `.ipynb` files
- `AI Diagonal` folder: Contains all AI conversation records; files starting with `[cn]` are in Chinese, `[EN]` are in English
- `Project Development Reflection`: The project reflection document
- `Notebook` folder: Contains the main notebook file `submit_EN.ipynb`
- `src` folder also includes historical file versions
