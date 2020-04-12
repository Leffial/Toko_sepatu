from pymongo import MongoClient

class Data:
    
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017')
        db = client['toko_sepatu']

        current = datetime.now()
        tahun = current.year
        bulan = current.month
        hari = current.day

        user = db["tabel_user"]
        user.create_index("username", unique=True)
        
        dict_user = [
            {"id": 1, "nama": "admin", "username":"admin", "password":"admin", "role_id":1},
            {"id": 2, "nama": "user", "username":"user", "password":"user", "role_id":2}
        ]
        user.insert_many(dict_user)

        laporan = db["tabel_laporan"]
        data_laporan = [
            {"id_barang": 1, "nama": "leffi", "alamat" : "rawamangun", "no_telepon" : "021953672231"},
            {"id_barang": 2, "nama": "leffi2", "alamat" : "cipinang", "no_telepon" : "02195363217"}
        ]
        laporan.insert_many(data_laporan)

        barang = db["tabel_barang"]
        data_barang = [
            {"id_barang":1, "nama_barang":"Sepatu", "keterangan":"Compass", "kategori":"public low","ukuran": "42", "harga":"250000"},
            {"id_barang": 2, "nama_barang":"Sepatu", "keterangan":"Ventela", "kategori":"public high","ukuran": "40", "harga":"200000"}
        ]
            
        result_barang = barang.insert_many(data_barang)
        result_id = result_barang.inserted_ids
        
        print(client.list_database_names())
        print(db.list_collection_names())
        
      
if __name__ == "__main__":
    Data()
