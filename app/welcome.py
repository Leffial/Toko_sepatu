from tkinter import *
import login

class WelcomeWindow:

    def __init__(self):
        self.win = Tk()

        self.canvas = Canvas(self.win, width=600, height=400,  bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+" + str(x) + "+" + str(y)
        
        self.win.geometry(str1)
        self.win.resizable(width=False, height=False)

        self.win.title("Welcome Administrator")

    def add_frame(self):
        self.frame = Frame(self.win, height=300, width= 450)
        self.frame.place(x=80,y=50)
        x,y = 70, 20

        self.img = PhotoImage(file='image/user1.png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x-85, y=-70)

        self.labeltitle = Label(self.frame, text="Selamat Datang")
        self.labeltitle.config(font=('Courier', 20, 'bold'))

        self.button = Button(self.frame, text="Ingin Belanja?Klik! ", font=('helevtica',20, 'bold'),bg='dark blue', fg='white', command = self.login)
        self.button.place(x=x+20, y= y+200)
        
        self.win.mainloop()

    def login(self):
        self.win.destroy()
        log = login.Login()
        log.add_frame()
