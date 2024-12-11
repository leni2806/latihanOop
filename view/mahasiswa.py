class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"{self.nim} - {self.nama} ({self.jurusan})"


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        for mhs in self.data:
            if mhs.nim == nim:
                self.data.remove(mhs)
                return True
        return False

    def ubah_data(self, nim, nama_baru, jurusan_baru):
        for mhs in self.data:
            if mhs.nim == nim:
                mhs.nama = nama_baru
                mhs.jurusan = jurusan_baru
                return True
        return False

    def cari_data(self, nim):
        for mhs in self.data:
            if mhs.nim == nim:
                return mhs
        return None

    def semua_data(self):
        return self.data
