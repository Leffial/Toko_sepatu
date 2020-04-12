from tkinter import *
import login
from pymongo import MongoClient
import controller_auth

class Administrator:
    def __init__(self):
        self.win = Tk()
        
        self.client = MongoClient('mongodb://localhost:27017')
        self.mydb = self.client['toko_sepatu']
        self.mycol = self.mydb['tabel_barang']
        self.mycol2 = self.mydb['tabel_laporan']
        
        self.canvas = Canvas(self.win, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1000 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "1000x500+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        self.win.resizable(width=False, height=False)

        self.win.title("Administrator")
        
    def halaman(self):
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

        text_harga = StringVar()
        self.label_harga = Label(self.frame, text="Harga")
        self.label_harga.config(font=("courier", 12, 'bold'))
        self.label_harga.place(x=30, y = 90)

        self.entry_harga = Entry(self.frame, font="Courier 10")
        self.entry_harga.place(x=200, y = 90)

        text_id = StringVar()
        self.label_id = Label(self.frame, text="Id Barang")
        self.label_id.config(font=("courier", 12, 'bold'))
        self.label_id.place(x=390, y = 10)

        self.entry_id = Entry(self.frame, font="Courier 10")
        self.entry_id.place(x=490, y = 10)
        
        self.button = Button(self.frame, text="Tambah Barang", font='Courier 12 bold', command= lambda: self.add_item(self.entry_id, self.entry_barang, self.entry_keterangan, self.entry_kategori, self.entry_ukuran, self.entry_harga))
        self.button.place(x=30, y= 125)

        self.button = Button(self.frame, text="Hapus barang", font='Courier 12 bold', command= lambda: self.delete_item(self.entry_id, self.entry_barang, self.entry_keterangan, self.entry_kategori, self.entry_ukuran, self.entry_harga))
        self.button.place(x=200, y= 125)

        self.button = Button(self.frame, text="Cek Laporan", font='Courier 12 bold', command = self.cek_laporan)
        self.button.place(x=370, y= 125)

        self.part_list = Listbox(self.frame, height=12,width=115,border=0)
        self.part_list.place(x=30, y=175)


        self.part_list.delete(0, END)
        self.part_list.insert(END, "Daftar Barang")
        for row in self.mycol.find({},{ "_id": 0, "id_barang" : 1, "nama_barang": 1, "keterangan": 1, "kategori": 1, "ukuran" : 1, "harga": 1 }):
            self.part_list.insert(END, row)

        self.button = Button(self.frame, text="Logout", font='Courier 12 bold', command= self.logout)
        self.button.place(x=30, y= 370)
        
        self.win.mainloop()

    def add_item(self, id_barang, nama_barang, keterangan, kategori, ukuran, harga):
        id_barang = self.entry_id.get()
        nama_barang = self.entry_barang.get()
        keterangan =  self.entry_keterangan.get()
        kategori = self.entry_kategori.get()
        ukuran = self.entry_ukuran.get()
        harga = self.entry_harga.get()
        obj = controller_auth.Controller()
        obj.ShowCek_item(id_barang, nama_barang, keterangan, kategori, ukuran, harga)
        

    def delete_item(self,id_barang, nama_barang, keterangan, kategori, ukuran, harga):
        id_barang = self.entry_id.get()
        nama_barang = self.entry_barang.get()
        keterangan =  self.entry_keterangan.get()
        kategori = self.entry_kategori.get()
        ukuran = self.entry_ukuran.get()
        harga = self.entry_harga.get()
        obj = controller_auth.Controller()
        obj.Showhapus_item(id_barang, nama_barang, keterangan, kategori, ukuran, harga)
    
    def cek_laporan(self):
        self.frame = Frame(self.win, height=400, width=900)
        self.frame.place(x=50,y=50)

        x,y = 0,0

        self.part_list = Listbox(self.frame, height=15,width=95,border=0)
        self.part_list.place(x=30, y=50)


        self.part_list.delete(0, END)
        self.part_list.insert(END, "Daftar Pemesan")
        for row in self.mycol2.find({},{ "_id": 0,"id_barang" : 1, "nama": 1, "alamat": 1, "no_telepon": 1, "ukuran" : 1, "harga": 1 }):
            self.part_list.insert(END, row)

        self.button = Button(self.frame, text="Kembali", font='Courier 12 bold', command = self.kembali)
        self.button.place(x=30, y= 350)
        self.button = Button(self.frame, text="Logout", font='Courier 12 bold', command= self.logout)
        self.button.place(x=530, y= 350)
        
        self.win.mainloop()
        
    def kembali(self):
        self.win.destroy()
        Administrator().halaman()
    
    def logout(self):
        self.win.destroy()
        log = login.Login()
        log.add_frame()

