#-*- coding: utf-8 -*-

#Proyecto final de Fundamentos de Sistemas Embebidos
#Centro Multimedia
#Desarolladores:
#Cadena Campos Luis
#Pineda Hernandez Isaac Jair
#Galvan Guevara Pedro Josue

#MIT License

from tkinter import *
from tkinter import ttk
from pygame import mixer
import webbrowser
import ctypes
import os
import vlc
import time
 
#Cargamos el cdll para arreglar el correcto uso del display
x11 = ctypes.cdll.LoadLibrary('libX11.so')
x11.XInitThreads()

#Función que abre el navegador chromium con el enlace predefinido.
def abreSpotify():
	navegador=webbrowser.get("chromium")
	navegador.open("https://open.spotify.com/",new=2, autoraise=True)

#Función que abre el navegador chromium con el enlace predefinido.
def abreDeezer():
	navegador=webbrowser.get("chromium")
	navegador.open("https://www.deezer.com/us/login",new=2, autoraise=True)

#Función que abre el navegador chromium con el enlace predefinido.
def abreTidal():
	navegador=webbrowser.get("chromium")
	navegador.open("https://login.tidal.com/authorize?client_id=jn73zEik7Fkhsa5B&lang=mx&redirect_uri=https%3A%2F%2Fmy.tidal.com%2Foauth%2Freturn&response_type=code&restrict_signup=true&state=e693eb8a-95cd-4a62-8bea-9538bdd63c41&geo=MX&campaignId=default",new=2, autoraise=True)

#Función que abre el navegador chromium con el enlace predefinido.
def abreNetflix():
	navegador=webbrowser.get("chromium")
	navegador.open("https://www.netflix.com/browse",new=2, autoraise=True)

#Función que abre el navegador chromium con el enlace predefinido.
def abrePrimeVideo():
	navegador=webbrowser.get("chromium")
	navegador.open("https://www.amazon.com/ap/signin?clientContext=134-3771376-0311117&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3Flocation%3D%2F%3Fref_%253Ddv_auth_ret&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_desktop_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",new=2, autoraise=True)

#Función que abre el navegador chromium con el enlace predefinido.
def abreDisneyplus():
	navegador=webbrowser.get("chromium")
	navegador.open("https://www.disneyplus.com/login/",new=2, autoraise=True)

#Función que despliega las usbs disponibles.
def navegacionUsb(root):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana con dimensiones especificas y se agrega un background
	ventana2 = Tk()
	ventana2.title("Selector de USB")
	ventana2.geometry('500x500')
	ventana2.config(bg="#8dc3d5")

	#Obtenemos todos los archivos de la usb
	path = "/media/pi/"
	#Creamos una lista con todos los archivos dentro de la usb
	usbs = os.listdir(path)
	#Creamos una bandera con el numero de usbs inicial
	numUsb = len(usbs)

	if len(usbs) > 0:
		#Creamos y asignamos el botón para entrar a la usb seleccionada
		botonUsb1=Button(ventana2,text=usbs[0],bg="#F64A5C",command=lambda:entrarUsb(ventana2,usbs[0]))
		botonUsb1.place(x=100,y=100)

		if len(usbs) > 1:
			#Creamos y asignamos el botón para entrar a la usb seleccionada
			botonUsb2=Button(ventana2,text=usbs[1],bg="#4AD55F",command=lambda:entrarUsb(ventana2,usbs[1]))
			botonUsb2.place(x=200,y=100)

			if len(usbs) > 2:
				#Creamos y asignamos el botón para entrar a la usb seleccionada
				botonUsb3=Button(ventana2,text=usbs[2],bg="#ECEA4E",command=lambda:entrarUsb(ventana2,usbs[2]))
				botonUsb3.place(x=300,y=100)

	#Creamos y asignamos el botón para regresar al menú de selección de funcionalidades
	botonRegresar=Button(ventana2,text="Regresar al Menu",bg="#F3CA65",command=lambda:principal(ventana2))
	botonRegresar.place(x=180,y=200)

	#Creamos ciclo para detectar un nuevo dispositivo
	try:
		while True:
			#Volvemos a crear una lista con los dispositivos disponibles
			buscaUsb = os.listdir(path)
			#Si tenemos los mismos dispositivos no hacemos nada
			if numUsb == len(buscaUsb):
				ventana2.update_idletasks()
				ventana2.update()
			else:
				#Si tenemos mas dispositivos que en la primera búsqueda refrescamos la ventana
				navegacionUsb(ventana2)
	except:
		print("Ventana actualizada")

#Función que despliega un menu para seleccionar un reproductor.
def entrarUsb(root,usb):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana con dimensiones especificas y se agrega un background
	ventana3 = Tk()
	ventana3.title("Reproductor")
	ventana3.geometry('500x500')
	ventana3.config(bg="#66D8C6")
	
	#Creamos y asignamos el botón para entrar al reproductor de música
	botonMusica=Button(ventana3,text="Musica",bg="#66D863",command=lambda:reproducirMusica(ventana3,usb))
	botonMusica.place(x=90,y=30) 
	
	#Creamos y asignamos el botón para entrar al reproductor de video
	botonVideo=Button(ventana3,text="Video",bg="#A272E4",command=lambda:reproducirVideo(ventana3,usb))
	botonVideo.place(x=240,y=30)
	
	#Creamos y asignamos el botón para entrar al reproductor de imagenes
	botonImagen=Button(ventana3,text="Fotos",bg="#69A6E7",command=lambda:reproducirImagen(ventana3,usb))
	botonImagen.place(x=360,y=30)

	#Creamos y asignamos el botón para regresar al menú de selección de dispositivos
	botonRegresar=Button(ventana3,text="Regresar a USBs disponibles",bg="#F3CA65",command=lambda:navegacionUsb(ventana3))
	botonRegresar.place(x=150,y=150)

#Función que despliega un menú para seleccionar un reproductor.
def usbDesconectada(root,usb):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana con dimensiones especificas y se agrega un background
	ventanaTemp = Tk()
	ventanaTemp.title("Dispositivo Desconectado")
	ventanaTemp.geometry('500x500')
	ventanaTemp.config(bg="#5FCC8F")

	#Creamos y asignamos etiqueta para describir el problema
	textoTemp=Label(ventanaTemp,text="Dispositivo ya no está disponible o está vacío")
	textoTemp.place(x=150,y=100)
	#Creamos y asignamos el botón para regresar al menú de selección de dispositivo
	botonRegresar=Button(ventanaTemp,text="Regresar",bg="#F64A5C",command=lambda:navegacionUsb(ventanaTemp))
	botonRegresar.place(x=250,y=200)

#Función que despliega el reproductor de música.
def reproducirMusica(root,usb):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana con dimensiones especificas y se agrega un background
	ventana4 = Tk()
	ventana4.title("Musica")
	ventana4.geometry('500x500')
	ventana4.config(bg="#66D863")

	try:
		#Obtenemos todos los archivos de la usb
		path = "/media/pi/" + usb
		#Creamos una lista con todos los archivos dentro de la usb
		archivos = os.listdir(path)

		#Creamos un array para guardar el archivo en reproducción
		numCancion = [0]
		#Creamos un array para guardar los archivos filtrados
		listaMusica = []

		#Destruimos la ventana de música y regresamos al menú multimedia
		def salirMedia(root,usb):
			mixer.music.stop()
			entrarUsb(root,usb)

		#Creamos array de archivos con extensión .mp3
		for item in archivos:
			if item.endswith(".mp3"): 
				listaMusica.append(item)

		#Comprobamos si el array filtrado está vacío.
		if len(listaMusica) == 0:
			#Creamos y asignamos etiqueta para describir el problema
			textoNoCanciones=Label(ventana4,text="Este dispositivo no tiene pistas.")
			textoNoCanciones.pack()
			#Creamos y asignamos el botón para regresar al menú de selección de usbs
			botonRegresar=Button(ventana4,text="Elegir otro reproductor",command=lambda:entrarUsb(ventana4,usb))
			botonRegresar.pack()
		else:
			#Listamos el array con etiquetas
			for cancion in listaMusica:
				textoCancion=Label(ventana4,text=cancion)
				textoCancion.pack()

			#Iniciamos el reproductor con la primer canción del array
			mixer.init()
			mixer.music.load("/media/pi/"+usb+"/"+listaMusica[numCancion[0]])
			mixer.music.set_volume(0.5)
			mixer.music.play()

			#Función que detiene la canción en reproducción e inicia la anterior
			def anterior(numCancion):
				#Si estamos en la última canción regresamos a la primera
				if numCancion[0] == 0:
					numCancion[0] = len(listaMusica)-1
				else:
					numCancion[0] -= 1
				#Detenemos el reproductor en ejecución
				mixer.music.stop()
				#Asignamos la ruta del archivo al reproductor
				mixer.music.load("/media/pi/"+usb+"/"+listaMusica[numCancion[0]])
				#Reproducimos el archivo asignado
				mixer.music.play()

			#Función que detiene la canción en reproducción e inicia la siguiente
			def siguiente(numCancion):
				#Si estamos en la primera canción regresamos a la última
				if numCancion[0] == len(listaMusica)-1:
					numCancion[0] = 0
				else:
					numCancion[0] +=1
				#Detenemos el reproductor en ejecución
				mixer.music.stop()
				#Asignamos la ruta del archivo al reproductor
				mixer.music.load("/media/pi/"+usb+"/"+listaMusica[numCancion[0]])
				#Reproducimos el archivo asignado
				mixer.music.play()

			#Creamos y asignamos el botón para reproducir el audio anterior
			botonAnterior=Button(ventana4,text="<<",bg="#F1C659",command=lambda:anterior(numCancion))
			botonAnterior.place(x=20,y=90)

			#Creamos y asignamos el botón para pausar la reproducción
			botonPausa=Button(ventana4,text="||",bg="#F1C659",command=lambda:mixer.music.pause())
			botonPausa.place(x=150,y=90)

			#Creamos y asignamos el botón para continuar con la reproducción pausada
			botonreanudar=Button(ventana4,text=" > ",bg="#F1C659",command=lambda:mixer.music.unpause())
			botonreanudar.place(x=250,y=90)

			#Creamos y asignamos el botón para reproducir el siguiente audio
			botonSiguiente=Button(ventana4,text=">>",bg="#F1C659",command=lambda:siguiente(numCancion))
			botonSiguiente.place(x=400,y=90)

			#Creamos y asignamos el botón para regresar al menú de selección de reproductor
			botonSalirMedia=Button(ventana4,text="Salir a media",bg="#66D8C6",command=lambda:salirMedia(ventana4,usb))
			botonSalirMedia.place(x=200,y=200)
	except:
		#Si no se puede acceder a la usb ejecutamos la función para regresar.
		usbDesconectada(ventana4,usb)

#Función que despliega el reproductor de video.
def reproducirVideo(root,usb):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana con dimensiones especificas y se agrega un background
	ventana5 = Tk()
	ventana5.title("Videos")
	ventana5.geometry('500x500')
	ventana5.config(bg="#A272E4")

	try:
		#Creamos y almacenamos la ruta para acceder a la usb
		path = "/media/pi/" + usb
		#Creamos una lista con todos los archivos dentro de la usb
		archivos = os.listdir(path)

		#Creamos un array para guardar los archivos filtrados
		listaVideos = []

		#Recorremos la lista con todos los archivos
		for item in archivos:
			#Filtramos los archivos que terminan con extensión .mp4
			if item.endswith(".mp4"):
				#Agregamos los archivos filtrados al final del array
				listaVideos.append(item)

		#Comprobamos si el array filtrado está vacío.
		if len(listaVideos) == 0:
			#Creamos y asignamos etiqueta para describir el problema
			textoNoVideos=Label(ventana5,text="Este dispositivo no tiene videos.")
			textoNoVideos.pack()
			#Creamos y asignamos el botón para regresar al menú de selección de usbs
			botonRegresar=Button(ventana5,text="Elegir otro reproductor",command=lambda:entrarUsb(ventana5,usb))
			botonRegresar.pack()
		else:
			#Creamos un array para pasar entre funciones con el reproductor
			medias=[]
			#Inicializamos el reproductor
			media = vlc.MediaPlayer(path+"/"+listaVideos[0])
			#Agregamos esl reproductor al array
			medias.append(media)

			#Función que reproduce el video seleccionado con el Radio Button
			def reproduceVid(lista,path,medias):
				#Detenemos el reproductor en ejecución
				medias[0].stop()
				#Asignamos la ruta del archivo al reproductor
				medias[0] = vlc.MediaPlayer(path+"/"+tipo.get())
				#Reproducimos el archivo asignado
				medias[0].play()

			#Función para detener el reproductor y salir de la ventana
			def salirMedia(root,usb,medias):
				#Detenemos el reproductor en ejecución
				medias[0].stop()
				#Salimos al menú de selección de reproductor
				entrarUsb(root,usb)

			#Listamos el array con etiquetas
			tipo=StringVar(value="a")
			for video in listaVideos:
				Radiobutton(ventana5,text=video,variable=tipo,value=video, command=lambda:reproduceVid(listaVideos,path,medias)).pack()

			#Creamos y asignamos el botón para regresar al menú de selección de reproductor
			botonSalirMedia=Button(ventana5,text="Salir a media",bg="#66D8C6",command=lambda:salirMedia(ventana5,usb,medias))
			botonSalirMedia.place(x=200,y=200)
	except:
		#Si no se puede acceder a la usb ejecutamos la función para regresar.
		usbDesconectada(ventana5,usb)

#Función que despliega el reproductor de imagenes.
def reproducirImagen(root,usb):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana con dimensiones especificas y se agrega un background
	ventana6 = Tk()
	ventana6.title("Imagenes")
	ventana6.geometry('500x500')
	ventana6.config(bg="#69A6E7")

	try:
		#Creamos y almacenamos la ruta para acceder a la usb
		path = "/media/pi/" + usb
		#Creamos una lista con todos los archivos dentro de la usb
		archivos = os.listdir(path)

		#Creamos un array para guardar los archivos filtrados
		listaImagenes = []

		#Recorremos la lista con todos los archivos
		for item in archivos:
			#Filtramos los archivos que terminan con extensión .jpg y .png
			if item.endswith((".jpg",".png")):
				#Agregamos los archivos filtrados al final del array
				listaImagenes.append(item)

		#Comprobamos si el array filtrado está vacío.
		if len(listaImagenes) == 0:
			#Creamos y asignamos etiqueta para describir el problema
			textoNoVideos=Label(ventana6,text="Este dispositivo no tiene imagenes.")
			textoNoVideos.pack()
			#Creamos y asignamos el botón para regresar al menú de selección de usbs
			botonRegresar=Button(ventana6,text="Elegir otro reproductor",command=lambda:entrarUsb(ventana6,usb))
			botonRegresar.pack()
		else:
			#Función que reproduce las imágenes en presentación.
			def muestraAlbum(album):
				#Recorremos el array con los archivos
				for imagen in listaImagenes:
					#Asignamos la ruta del archivo al reproductor
					media = vlc.MediaPlayer(path+"/"+imagen)
					#Reproducimos el archivo asignado
					media.play()
					#Esperamos tres segundos.
					time.sleep(3)
					#Detenemos el reproductor.
					media.stop()
            
            #Creamos y asignamos el botón para presentar las imagenes
			botonRepetir=Button(ventana6,text="Presentar imagenes",bg="#F3CA65",command=lambda:muestraAlbum(listaImagenes))
			botonRepetir.place(x=180,y=150)
			#Creamos y asignamos el botón para regresar al menú de selección de reproductor
			botonSalirMedia=Button(ventana6,text="Salir a media",bg="#66D8C6",command=lambda:entrarUsb(ventana6,usb))
			botonSalirMedia.place(x=200,y=250)
	except:
		#Si no se puede acceder a la usb ejecutamos la función para regresar.
		usbDesconectada(ventana6,usb)

#Función que despliega el menú de selección de funcionalidad.
def principal(root):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana con dimensiones especificas y se agrega un background
	ventana1 = Tk()
	ventana1.title("Centro Multimedia")
	ventana1.geometry('500x500')
	ventana1.config(bg="#8dc3d5")
    
    #Agregamos la foto para poner en el boton
	fotospotify=PhotoImage(file='spotify.png')
	#Crea boton que llama a la función abreSpotify.
	botonSpotify=Button(ventana1,image=fotospotify,command=abreSpotify)
	botonSpotify.place(x=20,y=30) #Marcamos las coordenadas del boton
	
	#Se crea el botón y se asigna la ventana de trabajo, la imagen de fondo 
	#y la función a ejecutar
	fotodeezer=PhotoImage(file='deezer.png')
	botonDeezer=Button(ventana1,image=fotodeezer,command=abreDeezer)
	botonDeezer.place(x=200,y=30)
	
	#Se crea el botón y se asigna la ventana de trabajo, la imagen de fondo 
	#y la función a ejecutar
	fototidal=PhotoImage(file='tidal.png')
	botonTidal=Button(ventana1,image=fototidal,command=abreTidal)
	botonTidal.place(x=380,y=30)
    
    #Se crea el botón y se asigna la ventana de trabajo, la imagen de fondo 
	#y la función a ejecutar
	fotonetflix=PhotoImage(file='netflix.png')
	botonNetflix=Button(ventana1,image=fotonetflix,command=abreNetflix)
	botonNetflix.place(x=20,y=90)
	
	#Se crea el botón y se asigna la ventana de trabajo, la imagen de fondo 
	#y la función a ejecutar
	fotoPrimeVideo=PhotoImage(file='primevideo.png') 
	botonPrimeVideo=Button(ventana1,image=fotoPrimeVideo,command=abrePrimeVideo)
	botonPrimeVideo.place(x=200,y=90)
	
	#Se crea el botón y se asigna la ventana de trabajo, la imagen de fondo 
	#y la función a ejecutar
	fotodisneyplus=PhotoImage(file='disneyplus.png')
	botonDisneyPlus=Button(ventana1,image=fotodisneyplus,command=abreDisneyplus)
	botonDisneyPlus.place(x=380,y=90)
	
	#Se crea el botón y se asigna la ventana de trabajo, la imagen de fondo 
	#y la función a ejecutar
	fotoUSB=PhotoImage(file='usb.png')
	botonUSB=Button(ventana1,image=fotoUSB,command=lambda:navegacionUsb(ventana1))
	botonUSB.place(x=220,y=170) 
	   
	#Se crea el botón y se asigna la ventana de trabajo, la imagen de fondo 
	#y se destruye la ventana actual
	fotoSalir=PhotoImage(file='salir.png') 
	botonSalir=Button(ventana1,image=fotoSalir,command=lambda:ventana1.destroy())
	botonSalir.place(x=180,y=270) 

	ventana1.mainloop()

#Función que despliega una ventana de inicio.
def main():
	#Inicializa la ventana con dimensiones especificas y se agrega un background
	ventana0 = Tk()
	ventana0.title("Inicio")
	ventana0.geometry('500x500')
	ventana0.config(bg="#8dc3d5")

	#Crea etiqueta y se asigna la ventana y el texto a mostrar
	textoInicio=Label(ventana0,text="Centro Multimedia FSE")
	textoInicio.pack()
	
	#Crea botón que llama a la función principal y se envia la ventana actual.
	fotoEmpezar=PhotoImage(file='inicio.png')
	botonEmpezar=Button(ventana0,image=fotoEmpezar,command=lambda:principal(ventana0))
	botonEmpezar.place(x=180,y=90)  

	ventana0.mainloop()

main()
