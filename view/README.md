# **Membuat Kode Program dari flowchart pertemuan ke 5**

Tugas Pertemuan Ke 5

Nama: Leni

Kelas: TI 24 A5

NIM: 312410442

## **1. bilanganterbesar.py**

Program **_bilanganterbesar.py_** adalah Program untuk menampilkan bilangan terbesar dari 3 buah Bilangan yang akan di Inputkan oleh user

Flowchart dari Program tersebut

<img src="/.images/pertama.png" width="500" alt="Flowchart">

**Program akan meminta kita untuk memasukkan 3 angka untuk dibandingkan :**

<img src="/.images/outputprogram1.png" width="500" alt="output">

**Penjelasan Code**

```
# Input tiga bilangan A, B, C
A = float(input("Masukkan bilangan A: "))
B = float(input("Masukkan bilangan B: "))
C = float(input("Masukkan bilangan C: "))

# Membandingkan nilai A, B, dan C untuk menentukan yang terbesar
if A > B and A > C:
    print("A adalah bilangan terbesar:", A)
elif B > C:
    print("B adalah bilangan terbesar:", B)
else:
    print("C adalah bilangan terbesar:", C)

```

1. Program meminta input tiga bilangan (A, B, C).
2. Kondisi pertama membandingkan apakah A lebih besar dari B dan C.
3. Jika benar, A adalah yang terbesar. Jika tidak, diperiksa apakah B lebih besar dari C. Jika ya, B yang terbesar.
4. Jika kedua kondisi tersebut tidak terpenuhi, maka C akan menjadi bilangan terbesar.

## **2. bilanganN.py**

Program **_bilanganN.py_** adalah untuk membandingkan bilangan yang di Input, input akan terus berjalan kecuali user memasukkan nilai 0

**Flowchartnya**

<img src="/.images/kedua.png" width="500" alt="Flowchart">

**Program akan meminta kita untuk memasukkan angka untuk dibandingkan, _`input akan terus diminta sebelum user memasukkan angka 0_ :**

<img src="/.images/outputprogram2.png" width="500" alt="output">

**Penjelasan Code**

```
def find_largest_number():
```

Mendefinisikan fungsi bernama _find_largest_number_ yang akan menangani logika utama program.

```
    largest = float('-inf')  # Inisialisasi dengan nilai negatif tak terhingga
```

Menginisialisasi variabel largest dengan nilai negatif tak terhingga. Ini memastikan bahwa angka pertama yang dimasukkan akan selalu lebih besar.

_\*Maksud dari -infinity(Negatif tak hingga) adalah nilai negatif berapapun._

```
    count = 0
```

Menginisialisasi variabel _count_ untuk menghitung jumlah bilangan yang dimasukkan.

```
    while True:
```

Memulai loop tak terbatas. Akan terus berjalan sampai dihentikan oleh _break_.

```
        num = float(input(f"Masukkan bilangan ke-{count + 1} (atau 0 untuk selesai): "))

```

Meminta input dari pengguna, mengkonversinya ke float, dan menyimpannya dalam variabel _num_.

```
if num == 0:
            break
```

Jika input adalah 0, keluar dari loop.

```
count += 1
```

Menambah penghitung jumlah bilangan yang dimasukkan.

```
if num > largest:
            largest = num
```

Jika bilangan yang baru dimasukkan lebih besar dari _largest_ saat ini, update _largest_.

```
return largest, count
```

Setelah loop selesai, kembalikan bilangan terbesar dan jumlah input.

```
print("Program untuk menentukan bilangan terbesar dari N bilangan")
print("Masukkan angka 0 untuk mengakhiri input\n")
```

Mencetak instruksi untuk pengguna.

```
largest, count = find_largest_number()
```

Memanggil fungsi _find_largest_number()_ dan menyimpan hasilnya.

```
if count > 0:
```

Memeriksa apakah ada bilangan yang dimasukkan.

```
print(f"\nJumlah bilangan yang dimasukkan: {count}")
    print(f"Bilangan terbesar adalah: {largest}")
```

Jika ada bilangan yang dimasukkan, cetak jumlah input dan bilangan terbesar.

```
else:
    print("\nTidak ada bilangan yang dimasukkan.")
```

Jika tidak ada bilangan yang dimasukkan (pengguna langsung memasukkan 0), program akan dijalankan dan menampilkan output perbandingan.
