import tkinter as tk
import requests
import time


def get_weather(canvas):
    city = textfield.get()
    # First API call: Get current weather + coordinates
    city_api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0d15f68348014be341cf956aa34f24b1&units=metric"
    city_data = requests.get(city_api).json()

    if city_data.get('cod') == 200:
        condition = city_data['weather'][0]['main']
        temp = int(city_data['main']['temp'])
        pressure = city_data['main']['pressure']
        humidity = city_data['main']['humidity']
        wind = city_data['wind']['speed']

        # ✅ Use Forecast API to calculate today's min/max
        forecast_api = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=0d15f68348014be341cf956aa34f24b1&units=metric"
        forecast_data = requests.get(forecast_api).json()

        min_temp = max_temp = "N/A"
        if "list" in forecast_data:
            today = time.strftime("%Y-%m-%d", time.gmtime(time.time() + city_data['timezone']))
            temps = []
            for entry in forecast_data["list"]:
                if entry["dt_txt"].startswith(today):
                    temps.append(entry["main"]["temp"])

            if temps:
                min_temp = int(min(temps))
                max_temp = int(max(temps))

        # Sunrise / Sunset with timezone offset
        timezone_offset = city_data['timezone']
        sunrise = time.strftime("%I:%M:%S %p", time.gmtime(city_data['sys']['sunrise'] + timezone_offset))
        sunset = time.strftime("%I:%M:%S %p", time.gmtime(city_data['sys']['sunset'] + timezone_offset))

        # Display with emojis 🌡️💧🌬️
        final_inf = f"🌤️ {condition}\n🌡️ {temp}°C"
        final_data = (
            f"\n🔺 Max Temp: {max_temp}°C"
            f"\n🔻 Min Temp: {min_temp}°C"
            f"\n🧭 Pressure: {pressure} hPa"
            f"\n💧 Humidity: {humidity}%"
            f"\n🌬️ Wind Speed: {wind} m/s"
            f"\n🌅 Sunrise: {sunrise}"
            f"\n🌇 Sunset: {sunset}"
        )

        label1.config(text=final_inf)
        label2.config(text=final_data)

    else:
        label1.config(text="❌ Invalid City Name")
        label2.config(text="Please enter a valid city.")


# ---------- GUI SETUP ----------
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("🌦️ Weather App")

f = ("poppins", 15, 'bold')
t = ("poppins", 35, 'bold')

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind("<Return>", lambda event: get_weather(canvas))

label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f, justify="left", anchor="w")
label2.pack()

canvas.mainloop()
