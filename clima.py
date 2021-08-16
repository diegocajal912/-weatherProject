from tkinter import *
import requests

#52f64bb3bc0696bd36dd12205f719e3b
#api.openweathermap.org/data/2.5/weather?q={city name}

def mostrar_respuesta(clima):
	try:
		nombre_cuidad = clima["name"]
		desc = clima["weather"][0]["description"]
		temp = clima["main"]["temp"]

		cuidad["text"] = nombre_cuidad
		temperatura["text"] = str(int(temp)) + "ºC"
		descripcion["text"] = desc
	except:
		cuidad["text"] = "Intenta nuevamente"

def clima_JSON(cuidad):
	try:
		API_key = "52f64bb3bc0696bd36dd12205f719e3b"
		URL = "https://api.openweathermap.org/data/2.5/weather"
		parametros = {"APPID" : API_key, "q" : cuidad, "units" : "metric", "lang" : "es"}
		response = requests.get(URL, params = parametros)
		clima= response.json()
		mostrar_respuesta(clima)
	except:
		print("Error")
	

ventana = Tk()
ventana.geometry("350x550")


texto_ciudad = Entry(ventana, font = ("Couruer", 20,"normal" ), justify = "center")
texto_ciudad.pack(padx = 30, pady= 30)

obtener_clima = Button(ventana, text = "Obtener Clima", font = ("Courier", 28, "normal"), command = lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

cuidad= Label(font = ("Courier", 20, "normal"))
cuidad.pack(padx=30, pady=30)

temperatura= Label(font = ("Courier", 50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion= Label(text = "weather", font = ("Courier", 20, "normal"))
descripcion.pack(padx=10, pady=10)


ventana.mainloop()