data = {}
# Memuat Class
class Data():
    def __init__(self,nama,nim,uts,uas,tugas,total):
              
# Menambahkan data
        print("Tambah Data")
    def tambah(self):
        self.nama = input("Nama           : ")
        self.nim = int(input("NIM            : "))
        self.uts = int(input("Nilai UTS      : "))
        self.uas = int(input("Nilai UAS      : "))
        self.tugas = int(input("Nilai Tugas    : "))
        self.total = self.uts*35/100 + self.uas*35/100 + self.tugas*30/100
        data[self.nama] = self.nim, self.uts, self.uas, self.tugas, self.total


# Menghapus data
    def hapus(self):
        print("Hapus Data")
        self.nama = input("Masukkan Nama  : ")
        if self.nama in data.keys():
            del data[self.nama]
        else:
            print("Nama {0} Tidak Ditemukan".format(self.nama))
        return

# Mengubah data
    def ubah(self):
        print("Ubah Data")
        self.nama = input("Masukkan Nama  : ")
        if self.nama in data.keys():
            self.nim = int(input("NIM            : "))
            self.uts = int(input("Nilai UTS      : "))
            self.uas = int(input("Nilai UAS      : "))
            self.tugas = int(input("Nilai Tugas    : "))
            self.total = self.uts*35/100 + self.uas*35/100 + self.tugas*30/100
            data[self.nama] = self.nim, self.uts, self.uas, self.tugas, self.total
        else:
            print("Nama {0} tidak ditemukan".format(self.nama))

