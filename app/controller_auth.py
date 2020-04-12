from tkinter import *
from tkinter import messagebox
from model_auth import Auth
from pymongo import MongoClient
import dashboard
import admin
import form_pesanan

class Controller:
    def __init__(self):
        self.win = Tk()
    
    def Showlogin(self,username,password):
       obj = Auth()
       x = obj.loginUser(username,password)
       y = obj.loginAdmin(username,password)
       if x :
        messagebox.showinfo("Login Berhasil")
        self.win.destroy()
        buka = dashboard.Dashboard()
        buka.add_menu()
       elif y :
        messagebox.showinfo("Sukses")
        self.win.destroy()
        buka1 = admin.Administrator()
        buka1.halaman()
       else:
        messagebox.showinfo("username/password salah")

    def Showpesan(self,nama_barang, keterangan, kategori, ukuran, harga):
        masuk = Auth()
        x = masuk.pushpesan(nama_barang, keterangan, kategori, ukuran, harga)
        if x:
            messagebox.showinfo("Berhasil Pesan")
            self.win.destroy()
            buka = form_pesanan.Pesanan()
            buka.Tambah()     
        else:
            messagebox.showinfo("Gagal Pesan")
            
    def ShowCek_item(self, id_barang, nama_barang, keterangan, kategori, ukuran, harga):
        masuk = Auth()
        x = masuk.add_item(id_barang, nama_barang, keterangan, kategori, ukuran, harga)
        if x:
            messagebox.showinfo("Berhasil")
            self.win.destroy()
            buka = admin.Administrator()
            buka.halaman()          
        else:
            messagebox.showinfo("Gagal")

    def Showhapus_item(self, id_barang, nama_barang, keterangan, kategori, ukuran, harga):
        masuk = Auth()
        x = masuk.delete_item(id_barang, nama_barang, keterangan, kategori, ukuran, harga)
        if x:
            messagebox.showinfo("Berhasil")
            self.win.destroy()
            buka = admin.Administrator()
            buka.halaman()           
        else:
            messagebox.showinfo("Gagal")
    def ShowPemesan(self, nama, alamat, no_telepon, id_barang):
        masuk = Auth()
        x = masuk.cek_pemesan(nama, alamat, no_telepon, id_barang)
        if x:
            messagebox.showinfo("Berhasil Pesan")
            self.win.destroy()
            buka = dashboard.Dashboard()
            buka.add_menu()
            
        else:
            messagebox.showinfo("Gagal pesan")
