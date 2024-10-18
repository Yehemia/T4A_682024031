from . import database
#Fungsi untuk menambahkan data    
def create_data():
    while True:
        Nama = input("Masukan Nama Mahasiswa\t: ").title()
        while(True):#mengecek NIM apakah sudah benar
            try:
                NIM = int(input("Masukan NIM Mahasiswa\t: "))
                if len(str(NIM)) == 9:#NIM harus 9 angka
                    break
                else:
                    print("NIM harus 9 angka, silahkan masukan NIM lagi")    
            except:
                print("NIM harus angka, silahkan masukan angka lagi")    
        
        Fakultas = input("Masukan Fakultas\t: ").title()
        Prodi = input("Masukan Program Studi\t: ").title()
        database.create(Nama,NIM,Fakultas,Prodi) # Menyimpan data ke dalam data.txt melalui fungsi database.create 
        print("Data Mahasiswa berhasil ditambahkan!")
            
        while True:
            lanjut = input("Apakah ingin menambah data mahasiswa lain? (y/t): ").lower()
            if lanjut == 'y':
                break  
            elif lanjut == 't':
                break  
            else:
                print("Masukan hanya y/n!")
            
        if lanjut == 't':
            break   
#Fungsi untuk menampilkan data            
def read_data():
    try:
        # Membuka file data.txt yang didefinisikan di dalam modul
        with open(database.db_name, 'r', encoding="utf-8") as file:
            data_file = file.readlines()
            
        print("="*15, "DAFTAR MAHASISWA", "="*15)

        for i, data in enumerate(data_file, start=1):
            # Memisahkan data berdasarkan koma
            data_split = data.strip().split(',')
            nama, nim, fakultas, prodi = data_split
            print(f'''Mahasiswa {i}:
  Nama     : {nama}
  NIM      : {nim}
  Fakultas : {fakultas}
  Prodi    : {prodi}
{"="*48}''')
                
    except FileNotFoundError:
        print("File database tidak ditemukan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
