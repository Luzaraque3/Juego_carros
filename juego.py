import random
from tkinter import *
from tkinter import messagebox

# comando del boton 
def jugar():
    messagebox.showinfo("Buena suerte", "El juego empzara")
    ventana_principal.delete("1.0", "end")

#variables globales
BASE = 560 
ALTURA = 360
RADIO = 50


ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("600x600")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="green")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="black", width=580, height=580)
frame_graficacion.place(x=10 , y=10)

c = Canvas (ventana_principal , width=BASE, height=ALTURA)
c.config(bg="gray")
c.place(x=20,y=20)

#
rectangulo = c.create_rectangle(0,0-100,0+120,ALTURA ,fill="firebrick1" )


# frame controles
frame_controles = Frame(ventana_principal) 
frame_controles.config(bg="coral", width=560, height=180)
frame_controles.place(x=20,y=400)
# boton de jugar
bt_jugar = Button(frame_controles,text="Jugar", command=jugar)
bt_jugar.place(x=235, y=85, width=100, height=30)

#carros
img_carro_1 = PhotoImage(file="Img/carro_1.avif")
carro_1 = c.create_image(BASE/3,ALTURA/3,image=img_carro_1)
#carros
"""img_carro_2 = PhotoImage(file="Img/carro2.png")
carro_2 = c.create_image(BASE/2,ALTURA/2,image=img_carro_2)"""


#desplegar ventana
ventana_principal.mainloop()












"""# -------------------
# variables globales
# -------------------
BASE = 460
ALTURA = 220
radio = 10
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2

centro_x = random.randint(radio, BASE)
centro_y = random.randint(radio, ALTURA)

def mover_pelota():
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, x1, y1 = c.coords(pelota)
    if x0 < 0 or x1 > BASE: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > ALTURA: 
        desplazamiento_y = -desplazamiento_y
    c.move(pelota, desplazamiento_x, desplazamiento_y)
    ventana_principal.after(intervalo, mover_pelota)

# -------------------
# ventana principal
# -------------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

# -------------------
# frame de graficacion
# -------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

pelota = c.create_oval(centro_x-radio, centro_y-radio, centro_x+radio, centro_y+radio, fill="green", outline="white")

mover_pelota()

# -------------------
# frame de controles
# -------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10,y=260)

# desplegar ventana
ventana_principal.mainloop()"""