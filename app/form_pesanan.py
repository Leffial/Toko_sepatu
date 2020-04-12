from tkinter import *
import login
from pymongo import MongoClient
import dashboard
import controller_auth

class Pesanan():
    def __init__(self):
        self.win = Tk()
        self.client = MongoClient('mongodb://localhost:27017')
        self.mydb = self.client['toko_sepatu']
        self.mycol = self.mydb['tabel_laporan']
        self.canvas = Canvas(self.win, width=400, height=350, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 350 / 2)
        str1 = "600x350+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        self.win.resizable(width=False, height=False)

        self.win.title("Form Pemesanan")

    def data_pemesan(self, nama, alamat, no_telepon, id_barang):
        id_barang = self.entry_id.get()
        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()
        no_telepon = self.entry_telepon.get()
        obj = controller_auth.Controller()
        obj.ShowPemesan(nama, alamat, no_telepon, id_barang)
        
        
    def Tambah(self):
        self.frame = Frame(self.win, height=300, width=450)
        self.frame.place(x=70,y=30)

        x,y = 0,0

        self.text_nama = StringVar()
        self.label_nama = Label(self.frame, text="Nama Lengkap ")
        self.label_nama.config(font=("courier", 12, 'bold'))
        self.label_nama.place(x=30, y = 10)

        self.entry_nama = Entry(self.frame, font="Courier 10")
        self.entry_nama.place(x=30, y = 30)

        self.text_alamat = StringVar()
        self.label_alamat = Label(self.frame, text="Alamat Lengkap")
        self.label_alamat.config(font=("courier", 12, 'bold'))
        self.label_alamat.place(x=30, y = 70)

        self.entry_alamat = Entry(self.frame, font="Courier 10")
        self.entry_alamat.place(x=30, y = 90)

        self.text_telepon = StringVar()
        self.label_telepon = Label(self.frame, text="No Telepon")
        self.label_telepon.config(font=("courier", 12, 'bold'))
        self.label_telepon.place(x=30, y = 130)

        self.entry_telepon = Entry(self.frame, font="Courier 10")
        self.entry_telepon.place(x=30, y = 150)

        self.text_id = StringVar()
        self.label_id = Label(self.frame, text="Id_barang")
        self.label_id.config(font=("courier", 12, 'bold'))
        self.label_id.place(x=230, y = 10)

        self.entry_id = Entry(self.frame, font="Courier 10")
        self.entry_id.place(x=230, y = 30)

        self.text_bca = StringVar()
        self.label_bca = Label(self.frame, text="Bank Bca => 123456")
        self.label_bca.config(font=("courier", 13, 'bold'))
        self.label_bca.place(x=230, y = 70)

        self.text_bri = StringVar()
        self.label_bri = Label(self.frame, text="Bank Bri => 654321")
        self.label_bri.config(font=("courier", 13, 'bold'))
        self.label_bri.place(x=230, y = 100)

        self.text_bni = StringVar()
        self.label_bni = Label(self.frame, text="Bank Bni => 012345")
        self.label_bni.config(font=("courier", 13, 'bold'))
        self.label_bni.place(x=230, y = 130)


        self.button = Button(self.frame, text="Pesan", font='Courier 12 bold',  command= lambda:self.data_pemesan(self.entry_nama, self.entry_alamat, self.entry_telepon, self.entry_id))
        self.button.place(x=30, y= 200)

        self.button = Button(self.frame, text="Kembali", font='Courier 12 bold', command = self.kembali) 
        self.button.place(x=30, y= 250)

        self.button = Button(self.frame, text="Logout", font='Courier 12 bold',command = self.logout)
        self.button.place(x=350, y= 250)
        
        self.win.mainloop()

    def logout(self):
        self.win.destroy()
        log = login.Login()
        log.add_frame()

    def kembali(self):
        self.win.destroy()
        buka = dashboard.Dashboard()
        buka.add_menu()
    
