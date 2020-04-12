from pymongo import MongoClient

class Auth:

    def __init__(self):
        client = MongoClient('mongodb://localhost:27017')
        db = client["toko_sepatu"]
        self.mycol = db["tabel_user"]
        self.mycol2 = db["tabel_barang"]
        self.mycol3 = db["tabel_laporan"]

    def loginUser(self,username,password):
        mydict = {"username" : username,"password" : password,"role_id" : 2}
        x = self.mycol.find_one(mydict)
        return x

    def loginAdmin(self,username,password):
        mydict1 = {"username" : username,"password" : password,"role_id" : 1}
        y = self.mycol.find_one(mydict1)
        return y
    
    def add_item(self, id_barang, nama_barang, keterangan, kategori, ukuran, harga):
        mydict = {'id_barang' : id_barang, 'nama_barang' : nama_barang,'keterangan' : keterangan,'kategori' : kategori, 'ukuran' : ukuran, 'harga' : harga}
        x = self.mycol2.insert_one(mydict)
        return x
        
    def delete_item(self,id_barang, nama_barang, keterangan, kategori, ukuran, harga):
        mydict = {'id_barang' : id_barang, 'nama_barang' : nama_barang,'keterangan' : keterangan,'kategori' : kategori, 'ukuran' : ukuran, 'harga' : harga}
        x = self.mycol2.delete_one(mydict)
        return x

    def pushpesan(self,nama_barang, keterangan, kategori, ukuran, harga):
        mydict = {'nama_barang' : nama_barang,'keterangan' : keterangan,'kategori' : kategori, 'ukuran' : ukuran, 'harga' : harga}
        x = self.mycol2.find_one(mydict)
        return x
        
    def cek_pemesan(self, nama, alamat, no_telepon, id_barang):
        mydict = {'id_barang' :id_barang, 'nama' : nama,'alamat' : alamat,'no_telepon' : no_telepon}
        x = self.mycol3.insert_one(mydict)
        return x
