from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

data_mahasiswa = DataMahasiswa()

def menu_utama():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Hapus Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_data()
            data_mahasiswa.tambah_data(Mahasiswa(nim, nama, jurusan))
            print("Data mahasiswa berhasil ditambahkan.")
        elif pilihan == "2":
            MahasiswaView.tampilkan_semua(data_mahasiswa.semua_data())
        elif pilihan == "3":
            nim = InputForm.input_nim()
            mahasiswa = data_mahasiswa.cari_data(nim)
            MahasiswaView.tampilkan_detail(mahasiswa)
        elif pilihan == "4":
            nim = InputForm.input_nim()
            mahasiswa = data_mahasiswa.cari_data(nim)
            if mahasiswa:
                nama_baru, jurusan_baru = InputForm.input_ubah_data()
                data_mahasiswa.ubah_data(nim, nama_baru, jurusan_baru)
                print("Data mahasiswa berhasil diubah.")
            else:
                print("Mahasiswa tidak ditemukan.")
        elif pilihan == "5":
            nim = InputForm.input_nim()
            if data_mahasiswa.hapus_data(nim):
                print("Data mahasiswa berhasil dihapus.")
            else:
                print("Mahasiswa tidak ditemukan.")
        elif pilihan == "6":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu_utama()
