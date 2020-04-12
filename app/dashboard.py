from tkinter import *
import login
import form_pesanan
import controller_auth
from pymongo import MongoClient

class Dashboard():
    def __init__(self):
        self.win = Tk()
        self.client = MongoClient('mongodb://localhost:27017')
        self.mydb = self.client['toko_sepatu']
        self.mycol = self.mydb['tabel_barang']
        self.canvas = Canvas(self.win, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1000 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "1000x500+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        self.win.resizable(width=False, height=False)

        self.win.title("Main Page")
        
    def pesan(self,nama_barang, keterangan, kategori, ukuran, harga):
        nama_barang = self.entry_barang.get()
        keterangan = self.entry_keterangan.get()
        kategori = self.entry_kategori.get()
        ukuran = self.entry_ukuran.get()
        harga = self.entry_harga.get()
        obj = controller_auth.Controller()
        obj.Showpesan(nama_barang, keterangan, kategori, ukuran, harga)
        
    def select_item(self,event):
        global selected_item
        self.index = self.part_list.curselection()[0]
        selected_item = self.part_list.get(self.index)
        #print(selected_item)
        
        self.entry_barang.delete(0, END)
        self.entry_barang.insert(END, selected_item[1])
        self.entry_keterangan.delete(0, END)
        self.entry_keterangan.insert(END, selected_item[1])
        self.entry_kategori.delete(0, END)
        self.entry_kategori.insert(END, selected_item[1])
        self.entry_ukuran.delete(0, END)
        self.entry_ukuran.insert(END, selected_item[1])
        self.entry_harga.delete(0, END)
        self.entry_harga.insert(END, selected_item[1])
        
        
    def add_menu(self):
        self.frame = Frame(self.win, height=400, width=900)
        self.frame.place(x=50,y=50)

        x,y = 0,0

        self.text_barang = StringVar()
        self.label_barang = Label(self.frame, text="Nama Barang ")
        self.label_barang.config(font=("courier", 12, 'bold'))
        self.label_barang.place(x=30, y = 10)

        self.entry_barang = Entry(self.frame, font="Courier 10")
        self.entry_barang.place(x=200, y = 10)

        self.text_keterangan = StringVar()
        self.label_keterangan = Label(self.frame, text="Keterangan")
        self.label_keterangan.config(font=("courier", 12, 'bold'))
        self.label_keterangan.place(x=30, y = 30)

        self.entry_keterangan = Entry(self.frame, font="Courier 10")
        self.entry_keterangan.place(x=200, y = 30)

        self.text_kategori = StringVar()
        self.label_kategori = Label(self.frame, text="Kategori")
        self.label_kategori.config(font=("courier", 12, 'bold'))
        self.label_kategori.place(x=30, y = 50)

        self.entry_kategori = Entry(self.frame, font="Courier 10")
        self.entry_kategori.place(x=200, y = 50)

        self.text_ukuran = StringVar()
        self.label_ukuran = Label(self.frame, text="Ukuran")
        self.label_ukuran.config(font=("courier", 12, 'bold'))
        self.label_ukuran.place(x=30, y = 70)

        self.entry_ukuran = Entry(self.frame, font="Courier 10")
        self.entry_ukuran.place(x=200, y = 70)

        self.text_harga = StringVar()
        self.label_harga = Label(self.frame, text="Harga")
        self.label_harga.config(font=("courier", 12, 'bold'))
        self.label_harga.place(x=30, y = 90)

        self.entry_harga = Entry(self.frame, font="Courier 10")
        self.entry_harga.place(x=200, y = 90)

        self.button = Button(self.frame, text="Pesan", font='Courier 12 bold', command= lambda:self.pesan(self.entry_barang, self.entry_keterangan, self.entry_kategori, self.entry_ukuran, self.entry_harga))
        self.button.place(x=30, y= 125)

        self.part_list = Listbox(self.frame, height=12,width=115,border=0)
        self.part_list.place(x=30, y=175)

        self.part_list.delete(0, END)
        self.part_list.insert(END, "Daftar Barang")
        for row in self.mycol.find({},{ "_id": 0,"id_barang" : 1, "nama_barang": 1, "keterangan": 1, "kategori": 1, "ukuran" : 1, "harga": 1 }):
            self.part_list.insert(END, row)
            
        self.part_list.bind('<<ListboxSelect>>', self.select_item)

        self.button = Button(self.frame, text="Logout", font='Courier 12 bold',command = self.logout)
        self.button.place(x=30, y= 370)
        
        self.win.mainloop()

    def logout(self):
        self.win.destroy()
        log = login.Login()
        log.add_frame()
