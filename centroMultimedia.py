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
 
x11 = ctypes.cdll.LoadLibrary('libX11.so')
x11.XInitThreads()


def abreSpotify():
	navegador=webbrowser.get("chromium")
	navegador.open("https://open.spotify.com/",new=2, autoraise=True)

def abreDeezer():
	navegador=webbrowser.get("chromium")
	navegador.open("https://www.deezer.com/us/login",new=2, autoraise=True)

def abreTidal():
	navegador=webbrowser.get("chromium")
	navegador.open("https://login.tidal.com/authorize?client_id=jn73zEik7Fkhsa5B&lang=mx&redirect_uri=https%3A%2F%2Fmy.tidal.com%2Foauth%2Freturn&response_type=code&restrict_signup=true&state=e693eb8a-95cd-4a62-8bea-9538bdd63c41&geo=MX&campaignId=default",new=2, autoraise=True)


def abreNetflix():
	navegador=webbrowser.get("chromium")
	navegador.open("https://www.netflix.com/browse",new=2, autoraise=True)

def abrePrimeVideo():
	navegador=webbrowser.get("chromium")
	navegador.open("https://www.amazon.com/ap/signin?clientContext=134-3771376-0311117&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3Flocation%3D%2F%3Fref_%253Ddv_auth_ret&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_desktop_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",new=2, autoraise=True)

def abreDisneyplus():
	navegador=webbrowser.get("chromium")
	navegador.open("https://www.disneyplus.com/login/",new=2, autoraise=True)

def navegacionUsb(root):
	root.destroy()
	ventana2 = Tk()
	ventana2.title("Selector de USB")
	ventana2.geometry('500x500')
	ventana2.config(bg="#8dc3d5")

	path = "/media/pi/"
	usbs = os.listdir(path)
	numUsb = len(usbs)

	if len(usbs) > 0:
		botonUsb1=Button(ventana2,text=usbs[0],bg="#F64A5C",command=lambda:entrarUsb(ventana2,usbs[0]))
		botonUsb1.place(x=100,y=100)

		if len(usbs) > 1:
			botonUsb2=Button(ventana2,text=usbs[1],bg="#4AD55F",command=lambda:entrarUsb(ventana2,usbs[1]))
			botonUsb2.place(x=200,y=100)

			if len(usbs) > 2:
				botonUsb3=Button(ventana2,text=usbs[2],bg="#ECEA4E",command=lambda:entrarUsb(ventana2,usbs[2]))
				botonUsb3.place(x=300,y=100)

	botonRegresar=Button(ventana2,text="Regresar al Menu",bg="#F3CA65",command=lambda:principal(ventana2))
	botonRegresar.place(x=180,y=200)

	try:
		while True:
			buscaUsb = os.listdir(path)
			if numUsb == len(buscaUsb):
				ventana2.update_idletasks()
				ventana2.update()
			else:
				navegacionUsb(ventana2)
	except:
		print("Ventana actualizada")

def entrarUsb(root,usb):
	root.destroy()
	ventana3 = Tk()
	ventana3.title("Reproductor")
	ventana3.geometry('500x500')
	ventana3.config(bg="#66D8C6")
	 
	botonMusica=Button(ventana3,text="Musica",bg="#66D863",command=lambda:reproducirMusica(ventana3,usb))
	botonMusica.place(x=90,y=30) 
	
	botonVideo=Button(ventana3,text="Video",bg="#A272E4",command=lambda:reproducirVideo(ventana3,usb))
	botonVideo.place(x=240,y=30)
	
	botonImagen=Button(ventana3,text="Fotos",bg="#69A6E7",command=lambda:reproducirImagen(ventana3,usb))
	botonImagen.place(x=360,y=30)

	botonRegresar=Button(ventana3,text="Regresar a USBs disponibles",bg="#F3CA65",command=lambda:navegacionUsb(ventana3))
	botonRegresar.place(x=150,y=150)

def usbDesconectada(root,usb):
	root.destroy()
	ventanaTemp = Tk()
	ventanaTemp.title("Dispositivo Desconectado")
	ventanaTemp.geometry('500x500')
	ventanaTemp.config(bg="#5FCC8F")
	textoTemp=Label(ventanaTemp,text="Dispositivo ya no está disponible o está vacío")
	textoTemp.place(x=150,y=100)
	botonRegresar=Button(ventanaTemp,text="Regresar",bg="#F64A5C",command=lambda:navegacionUsb(ventanaTemp))
	botonRegresar.place(x=250,y=200)

def reproducirMusica(root,usb):
	root.destroy()
	ventana4 = Tk()
	ventana4.title("Musica")
	ventana4.geometry('500x500')
	ventana4.config(bg="#66D863")

	try:
		#Obtenemos todos los archivos de la usb
		path = "/media/pi/" + usb
		archivos = os.listdir(path)

		numCancion = [0]
		listaMusica = []

		#Destruimos la ventana de música y regresamos al menú multimedia
		def salirMedia(root,usb):
			mixer.music.stop()
			entrarUsb(root,usb)

		#Creamos array de archivos con extensión .mp3
		for item in archivos:
			if item.endswith(".mp3"): 
				listaMusica.append(item)

		if len(listaMusica) == 0:
			textoNoCanciones=Label(ventana4,text="Este dispositivo no tiene pistas.")
			textoNoCanciones.pack()
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
				mixer.music.stop()
				mixer.music.load("/media/pi/"+usb+"/"+listaMusica[numCancion[0]])
				mixer.music.play()

			#Función que detiene la canción en reproducción e inicia la siguiente
			def siguiente(numCancion):
				#Si estamos en la primera canción regresamos a la última
				if numCancion[0] == len(listaMusica)-1:
					numCancion[0] = 0
				else:
					numCancion[0] +=1
				mixer.music.stop()
				mixer.music.load("/media/pi/"+usb+"/"+listaMusica[numCancion[0]])
				mixer.music.play()

			
			botonAnterior=Button(ventana4,text="<<",bg="#F1C659",command=lambda:anterior(numCancion))
			botonAnterior.place(x=20,y=90)

			
			botonPausa=Button(ventana4,text="||",bg="#F1C659",command=lambda:mixer.music.pause())
			botonPausa.place(x=150,y=90)

			
			botonreanudar=Button(ventana4,text=" > ",bg="#F1C659",command=lambda:mixer.music.unpause())
			botonreanudar.place(x=250,y=90)

			
			botonSiguiente=Button(ventana4,text=">>",bg="#F1C659",command=lambda:siguiente(numCancion))
			botonSiguiente.place(x=400,y=90)

			botonSalirMedia=Button(ventana4,text="Salir a media",bg="#66D8C6",command=lambda:salirMedia(ventana4,usb))
			botonSalirMedia.place(x=200,y=200)
	except:
		usbDesconectada(ventana4,usb)

def reproducirVideo(root,usb):
	root.destroy()
	ventana5 = Tk()
	ventana5.title("Videos")
	ventana5.geometry('500x500')
	ventana5.config(bg="#A272E4")

	try:
		path = "/media/pi/" + usb
		archivos = os.listdir(path)

		listaVideos = []

		#Creamos array de archivos con extensión .mp4
		for item in archivos:
			if item.endswith(".mp4"):
				listaVideos.append(item)

		if len(listaVideos) == 0:
			textoNoVideos=Label(ventana5,text="Este dispositivo no tiene videos.")
			textoNoVideos.pack()
			botonRegresar=Button(ventana5,text="Elegir otro reproductor",command=lambda:entrarUsb(ventana5,usb))
			botonRegresar.pack()
		else:
			medias=[]
			media = vlc.MediaPlayer(path+"/"+listaVideos[0])
			medias.append(media)

			def reproduceVid(lista,path,medias):
				medias[0].stop()
				medias[0] = vlc.MediaPlayer(path+"/"+tipo.get())
				medias[0].play()

			def salirMedia(root,usb,medias):
				medias[0].stop()
				entrarUsb(root,usb)

			#Listamos el array con etiquetas
			tipo=StringVar(value="a")
			for video in listaVideos:
				Radiobutton(ventana5,text=video,variable=tipo,value=video, command=lambda:reproduceVid(listaVideos,path,medias)).pack()

			botonSalirMedia=Button(ventana5,text="Salir a media",bg="#66D8C6",command=lambda:salirMedia(ventana5,usb,medias))
			botonSalirMedia.place(x=200,y=200)
	except:
		usbDesconectada(ventana5,usb)

def reproducirImagen(root,usb):
	root.destroy()
	ventana6 = Tk()
	ventana6.title("Imagenes")
	ventana6.geometry('500x500')
	ventana6.config(bg="#69A6E7")

	try:
		path = "/media/pi/" + usb
		archivos = os.listdir(path)

		listaImagenes = []

		#Creamos array de archivos con extensión .mp4
		for item in archivos:
			if item.endswith((".jpg",".png")):
				listaImagenes.append(item)

		if len(listaImagenes) == 0:
			textoNoVideos=Label(ventana6,text="Este dispositivo no tiene imagenes.")
			textoNoVideos.pack()
			botonRegresar=Button(ventana6,text="Elegir otro reproductor",command=lambda:entrarUsb(ventana6,usb))
			botonRegresar.pack()
		else:
			def muestraAlbum(album):
				for imagen in listaImagenes:
					media = vlc.MediaPlayer(path+"/"+imagen)
					media.play()
					time.sleep(3)
					media.stop()
            
			botonRepetir=Button(ventana6,text="Presentar imagenes",bg="#F3CA65",command=lambda:muestraAlbum(listaImagenes))
			botonRepetir.place(x=180,y=150)
			botonSalirMedia=Button(ventana6,text="Salir a media",bg="#66D8C6",command=lambda:entrarUsb(ventana6,usb))
			botonSalirMedia.place(x=200,y=250)
	except:
		usbDesconectada(ventana6,usb)

def principal(root):
	root.destroy()

	ventana1 = Tk()
	ventana1.title("Centro Multimedia")
	ventana1.geometry('500x500')
	ventana1.config(bg="#8dc3d5")
    
    #Agregamos las fotos para ponerlas en los botones
	fotospotify=PhotoImage(file='spotify.png')
	botonSpotify=Button(ventana1,image=fotospotify,command=abreSpotify)
	botonSpotify.place(x=20,y=30) #Marcamos las coordenadas del boton
	
	fotodeezer=PhotoImage(file='deezer.png')
	botonDeezer=Button(ventana1,image=fotodeezer,command=abreDeezer)
	botonDeezer.place(x=200,y=30)
	
	fototidal=PhotoImage(file='tidal.png')
	botonTidal=Button(ventana1,image=fototidal,command=abreTidal)
	botonTidal.place(x=380,y=30)
    
	fotonetflix=PhotoImage(file='netflix.png')
	botonNetflix=Button(ventana1,image=fotonetflix,command=abreNetflix)
	botonNetflix.place(x=20,y=90)
	
	fotoPrimeVideo=PhotoImage(file='primevideo.png') 
	botonPrimeVideo=Button(ventana1,image=fotoPrimeVideo,command=abrePrimeVideo)
	botonPrimeVideo.place(x=200,y=90)
	
	fotodisneyplus=PhotoImage(file='disneyplus.png')
	botonDisneyPlus=Button(ventana1,image=fotodisneyplus,command=abreDisneyplus)
	botonDisneyPlus.place(x=380,y=90)
	
	fotoUSB=PhotoImage(file='usb.png')
	botonUSB=Button(ventana1,image=fotoUSB,command=lambda:navegacionUsb(ventana1))
	botonUSB.place(x=220,y=170) 
	   
	fotoSalir=PhotoImage(file='salir.png') 
	botonSalir=Button(ventana1,image=fotoSalir,command=lambda:ventana1.destroy())
	botonSalir.place(x=180,y=270) 

	ventana1.mainloop()

def main():
	ventana0 = Tk()
	ventana0.title("Inicio")
	ventana0.geometry('500x500')
	ventana0.config(bg="#8dc3d5")


	textoInicio=Label(ventana0,text="Centro Multimedia FSE")
	textoInicio.pack()
	
	fotoEmpezar=PhotoImage(file='inicio.png')
	botonEmpezar=Button(ventana0,image=fotoEmpezar,command=lambda:principal(ventana0))
	botonEmpezar.place(x=180,y=90)  

	ventana0.mainloop()

main()