nama_pengguna = None  # Inisialisasi variabel global

def set_nama_pengguna(name):
    global nama_pengguna
    nama_pengguna = name

def get_nama_pengguna():
    return nama_pengguna