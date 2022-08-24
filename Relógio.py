from tkinter import *
from datetime import *
import pygame

cor1 = "#242323"
cond = False

hr = 0
min = 0
sec = 0

meses = ("","Jan","Fev",
"Mar","Abr","Maio","Jun",
"Jul","Ago","Set",
"Out","Nov","Dez")

data = ""

tempo = "00:00:00"
count = -3
cond = False

def clock():

    def time():
        global hr, min, sec, data, meses

        if cond == True:
            sec = str(0) + str(sec)
            min = str(0) + str(min)
            hr = str(0) + str(hr)

            crono["text"] = str(hr[-2:]) + ":" + str(min[-2:]) + ":" + str(sec[-2:])
            info["text"] = data

            crono.after(1000, time)
            hr = datetime.today().hour
            min = datetime.today().minute
            sec = datetime.today().second
            data = f"{date.today().day}/{meses[date.today().month]}"


    def start():
        global cond
        cond = True
        inic["state"] = "disabled"
        time()


    corbg = "#242323"

    mainclock = Tk()
    mainclock.title("RELÓGIO")
    mainclock.geometry("500x230+700+300")
    mainclock.config(bg = "#242323")
    mainclock.resizable(width = False, height = False)


    crono = Label(mainclock, text="00:00:00", font=("Courier 70 bold"), bg=corbg, fg="#16f59f")
    crono.place(x=25,y=20)

    info = Label(mainclock, text="", font=("Courier 24 bold"), bg=corbg, fg="#ac12c7")
    info.place(x=30,y=180)

    inic = Button(mainclock, text="Start", command = start, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
    inic.place(x=380, y= 160)

def crono():

    def time():
        global tempo
        global count

        if cond == True:
            if count <= -1:
                inicio = "Começando em " + str(count)[-1:]
                crono["text"] = inicio
                crono["font"] = "Courier 36 bold"
            else:
                crono["font"] = "Courier 70 bold"
                hr, min, sec = map(int, tempo.split(":"))
                sec = count
                
                if sec == 59:
                    count = -1
                    min += 1
                
                if min == 59:
                    min = 0
                    hr += 1

                sec = str(0) + str(sec)
                min = str(0) + str(min)
                hr = str(0) + str(hr)

                crono["text"] = str(hr[-2:]) + ":" + str(min[-2:]) + ":" + str(sec[-2:])
                tempo = str(hr[-2:]) + ":" + str(min[-2:]) + ":" + str(sec[-2:])
                
            crono.after(1000, time)
            count += 1
            inic["state"] = "disabled"

    def start():
        global cond
        cond = True
        time()

    def pause():
        global cond
        cond = False
        inic["state"] = "active"
        time()

    def resett():
        global tempo, count
        count = 0
        crono["text"] = "00:00:00"
        
    corbg = "#242323"

    maincrono = Tk()
    maincrono.title("CRONÔMETRO")
    maincrono.geometry("500x230+700+300")
    maincrono.config(bg = corbg)
    maincrono.resizable(width = False, height = False)
        
    crono = Label(maincrono, text= tempo, font=("Courier 70 bold"), bg=corbg, fg="#c21b2c")
    crono.place(x=25,y=20)


    inic = Button(maincrono, text="Iniciar", command = start, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
    inic.place(x=25, y= 160)

    pausa = Button(maincrono, text="Pausar", command = pause, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
    pausa.place(x=207, y= 160)

    reset = Button(maincrono, text="Resetar", command = resett, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
    reset.place(x=370, y= 160)

def timer():

    def timerzin():
        global hr, min, sec, cond
        
        if str(hr)[-2:] == "00" and str(min)[-2:] == "00" and str(sec)[-2:] == "00":
            label_crono["text"] = "00:00:00"
            pygame.init()
            pygame.mixer.music.load(r".alarm.mp3")
            pygame.mixer.music.play()
            pygame.event.wait()

        else:
            if cond == True:

                if int(sec) <= 0:
                    if int(min) > 0:
                        min = int(min) - 1
                        sec = 59
                    
                if int(min) <= 0 and int(sec) <= 0:
                    if int(hr) > 0:
                        hr = int(hr) - 1
                        min = 60

                sec = str(0) + str(sec)
                min = str(0) + str(min)
                hr = str(0) + str(hr)

                label_crono["text"] = str(hr[-2:]) + ":" + str(min[-2:]) + ":" + str(sec[-2:])

            if int(sec) > 0:
                sec = int(sec) - 1
            label_crono.after(1000, timerzin)
            entry_hr.delete(0, END)
            entry_min.delete(0, END)
            entry_sec.delete(0, END)

    def dados():
        global hr, min, sec
        hr = entry_hr.get()
        min = entry_min.get()
        sec = entry_sec.get()
        if hr == "":
            hr = "0"
        if min == "":
            min = "0"
        if sec == "":
            sec = "0"
        timerzin()

    def start():    
        global cond
        cond = True
        button_start["state"] = "disabled"
        dados()

    maintimer = Tk()
    maintimer.title("Timer")
    maintimer.geometry("600x350+650+300")
    maintimer.configure(bg= cor1)
    maintimer.resizable(height=False,width=False)


    label_hr = Label(maintimer, width=15, text="Horas", bg=cor1, fg= "white", font=("Courier 15 bold"))
    label_hr.grid(row=0, column= 0, padx=7, pady=20)

    label_min = Label(maintimer, width=15, text="Minutos", bg=cor1, fg= "white", font=("Courier 15 bold"))
    label_min.grid(row=0, column= 1, padx=7, pady=20)

    label_sec = Label(maintimer, width=15, text="Segundos", bg=cor1, fg= "white", font=("Courier 15 bold"))
    label_sec.grid(row=0, column= 2, padx=5, pady=20)

    label_crono = Label(maintimer, text= "00:00:00", bg=cor1, fg="#16f59f", font="Courier 85 bold")
    label_crono.place(x=25, y=110)


    entry_hr = Entry(maintimer, width=7, font="Arial 15")
    entry_hr.grid(row=1, column=0)

    entry_min = Entry(maintimer, width=7, font="Arial 15")
    entry_min.grid(row=1, column=1)

    entry_sec = Entry(maintimer, width=7, font="Arial 15")
    entry_sec.grid(row=1, column=2)

    button_start = Button(maintimer, text="Start", command=start, relief="solid", overrelief="ridge", bg=cor1, fg= "white", font="Courier 15 bold")
    button_start.place(x=260, y=260)

menu = Tk()
menu.title("")
menu.geometry("700x300+700+300")
menu.config(bg = "#242323")
menu.resizable(width = False, height = False)


label = Label(menu, text= "========== APLICAÇÕES ==========", bg=cor1, fg="white", font=("Gabriola 35 bold")).pack(pady=5)

botao = Button(menu, width=11, command= clock, text="Relógio", relief="solid", overrelief="ridge", bg=cor1, fg= "white", font="Courier 15 bold italic").pack(side=LEFT, padx=60)

botao3 = Button(menu, width=11, command= timer, text="Timer", relief="solid", overrelief="ridge", bg=cor1, fg= "white", font="Courier 15 bold italic").pack(side=RIGHT, padx=60)

botao2 = Button(menu, width=12, command= crono, text="Cronômetro", relief="solid", overrelief="ridge", bg=cor1, fg= "white", font="Courier 15 bold italic").pack(pady=35)


menu.mainloop()