class InputForm:
    @staticmethod
    def input_data():
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        return nim, nama, jurusan

    @staticmethod
    def input_nim():
        return input("Masukkan NIM: ")

    @staticmethod
    def input_ubah_data():
        nama_baru = input("Masukkan Nama Baru: ")
        jurusan_baru = input("Masukkan Jurusan Baru: ")
        return nama_baru, jurusan_baru
