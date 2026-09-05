# Tugas 1 RPL - SSD1030

A lightweight desktop application built with Python and Tkinter that integrates with the Google Gemini API to deliver smart weather forecasts and daily activity recommendations.

## About the Application
This application combines a user-friendly Graphical User Interface (GUI) with artificial intelligence. Instead of just displaying plain weather data, it leverages Google Gemini AI to analyze weather conditions and provide personalized daily advice, such as suggested clothing or outdoor activity reminders.

## System Architecture and Components
- Graphical Interface (app_ui.py): Built using Tkinter to provide a desktop window where users can enter a city name and view the weather analysis.
- Application Launcher (weather_app.py): Serves as the main entry point of the project, loading configurations and launching the GUI automatically.
- AI Integration: Uses the Google Gemini API to process weather prompts and generate contextual recommendations.

## Security and Best Practices
- Credential Protection: Sensitive information like your API key is kept locally in config.json, while config.json.example is uploaded to the repository as a reference template.
- Version Control Rules: The .gitignore file prevents sensitive local configs, temporary files, and Python build caches from being published to GitHub.

## Getting Started

1. Clone the Repository
   git clone https://github.com/NezzyGremory/SSD1030_Tugas1_60124030.git
   cd SSD1030_Tugas1_60124030

2. Setup Configuration
   Copy config.json.example and rename it to config.json.
   Add your Google Gemini API key to the api_key field inside config.json.

3. Run the Application
   python weather_app.py