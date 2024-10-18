# Nama file untuk menyimpan data mahasiswa
db_name = "data.txt"
#truktur dasar untuk menyimpan data
template = {
    "Nama": "nama",
    "NIM": "nim",
    "Fakultas": "fakultas",
    "Prodi": "prodi"
}
#fungsi untuk menambahkan data mahasiswa baru ke dalam file 
def create(Nama, NIM, Fakultas, Prodi):
    data = template.copy()

    data["Nama"] = Nama
    data["NIM"] = NIM
    data["Fakultas"] = Fakultas
    data["Prodi"] = Prodi

    data_str = f'{data["Nama"]},{data["NIM"]},{data["Fakultas"]},{data["Prodi"]}\n'
    try:
        # menambahkan data mahasiswa ke dalam file
        with open(db_name, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data Gagal ditambahkan")

# Fungsi untuk membaca data dari file data.txt
def read():
    try:
        with open(db_name, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False    