from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import dashboard
import admin
import controller_auth

class Login():

    def __init__(self):
        self.win = Tk()
        self.canvas = Canvas(self.win, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        
        self.win.geometry(str1)
        self.win.resizable(width=False, height=False)

        self.win.title( "Login")
    def add_frame(self):
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=80,y=50)

        x,y = -10,0

        self.img = PhotoImage(file='image/user1.png')
        self.label = Label(self.frame, image = self.img)
        self.label.place(x=x-30,y=y-80)

        self.label = Label(self.frame, text="Form Login")
        self.label.config(font=("courier", 20, 'bold'))
        self.label.place(x=130, y = y + 100)

        self.emlabel = Label(self.frame, text="Username")
        self.emlabel.config(font=("courier", 12, 'bold'))
        self.emlabel.place(x=100, y = y + 270)

        self.username = Entry(self.frame, font="Courier 10")
        self.username.place(x=190, y = 270)
        
        self.pslabel = Label(self.frame, text="Password")
        self.pslabel.config(font=("courier", 12, 'bold'))
        self.pslabel.place(x=100, y = y + 310)

        self.password = Entry(self.frame,show="*", font="Courier 10")
        self.password.place(x=190, y = 310)

        self.button = Button(self.frame, text="Masuk", font='Courier 15 bold', command= lambda: self.login(self.username, self.password))
        self.button.place(x=170, y= 350)

        self.win.mainloop()
      
    def login(self,username,password):
        username = self.username.get()
        password = self.password.get()
        obj = controller_auth.Controller()
        obj.Showlogin(username,password)
