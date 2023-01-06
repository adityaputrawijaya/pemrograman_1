data = {}
# Memuat Class
class Data():
    def __init__(self,nama,nim,uts,uas,tugas,total):

        while True:
            user = input("\n(T)ambah, (U)bah, (H)apus, (L)ihat, (K)eluar: ")
            if user == 'k':
                print("Program Selesai Terima kasih")
                break
            elif user == 't':
                self.tambah()
            elif user == 'l':
                self.tampilkan()
            elif user == 'h':
                self.hapus()
            elif user == 'u':
                self.ubah()