import os #import os untuk sistem operasi
import Dtbs as Db #import modul Dtbs 

# Fungsi untuk membuat gambar rumah
def gambar_rumah(tinggi_atap=5, lebar_atap=9):
    for i in range(tinggi_atap):
        bintang = '*' * (2 * i + 1)
        print(bintang.center(lebar_atap))
        
    tinggi_badan = tinggi_atap
    for i in range(tinggi_badan - 1):
        if i == 0:
            print('*' + ' ' * (lebar_atap - 2) + '*')
        else:
            print('*' + ' ' * (lebar_atap - 2) + '*')
    print('*' * lebar_atap,'\n')

# Fungsi utama untuk menjalankan program
def main():
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    gambar_rumah()
    
    while True:
        # Menu input data mahasiswa
        print("="*10, "MENU INPUT DATA MAHASISWA", "="*11)
        print(f"1. Tambah Data Mahasiswa")
        print(f"2. Lihat Data Mahasiswa")
        print(f"3. Keluar")
        print("="*48)
        user_option = input("Pilih menu (1-3): ")# Input user
        if user_option == "1":
            Db.create_data()
        elif user_option == "2":
            Db.read_data()
        elif user_option == "3":
            print("Keluar dari program")
            break

 # Memanggil fungsi main saat program dijalankan      
if __name__ == "__main__":
    main()  