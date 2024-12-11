class MahasiswaView:
    @staticmethod
    def tampilkan_semua(data_mahasiswa):
        print("\n--- Data Mahasiswa ---")
        for mhs in data_mahasiswa:
            print(mhs)
        print("----------------------")

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("\n--- Detail Mahasiswa ---")
            print(mahasiswa)
            print("------------------------")
        else:
            print("Mahasiswa tidak ditemukan.")
