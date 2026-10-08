import json
import os

# Nama file untuk simpan data inventaris
FILE_NAME = "inventaris.json"

def muat_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def simpan_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def tampilkan_data(data):
    print("           DAFTAR INVENTARIS BARANG GUDANG")
    print("=" * 50)
    
    if not data:
        print("Belum ada data barang di dalam inventaris.")
    else:
        print(f"{'No':<5} {'ID Barang':<12} {'Nama Barang':<20} {'Jumlah':<8} {'Harga (Rp)'}")
        print("-" * 50)
        for i, item in enumerate(data, start=1):
            print(f"{i:<5} {item['id']:<12} {item['nama']:<20} {item['jumlah']:<8} {item['harga']}")
    print("=" * 50)

def tambah_barang(data):
    print("\n--- Tambah Barang Baru ---")
    id_barang = input("Masukkan ID Barang      : ").strip()
    
    # untuk ngecek apakah ID sudah ada
    for item in data:
        if item['id'] == id_barang:
            print("Peringatan: ID Barang tersebut sudah ada di inventaris!")
            return

    nama_barang = input("Masukkan Nama Barang    : ").strip()
    
    try:
        jumlah = int(input("Masukkan Jumlah Stok    : "))
        harga = int(input("Masukkan Harga Satuan   : "))
    except ValueError:
        print("Kesalahan: Jumlah dan Harga harus angka!")
        return

    # Bikin dictionary data barang baru
    barang_baru = {
        "id": id_barang,
        "nama": nama_barang,
        "jumlah": jumlah,
        "harga": harga
    }

    # Tambah (append) ke list data simpan ke file
    data.append(barang_baru)
    simpan_data(data)
    print(f"Sukses: Barang '{nama_barang}' berhasil ditambah dan disimpan!")

def main():
    data_inventaris = muat_data()

    while True:
        print("SISTEM MANAJEMEN INVENTARIS TOKO")
        print("1. Lihat Daftar Barang")
        print("2. Tambah Barang Baru")
        print("3. Keluar Program")
        
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            tampilkan_data(data_inventaris)
        elif pilihan == "2":
            tambah_barang(data_inventaris)
        elif pilihan == "3":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1, 2, atau 3.")

if __name__ == "__main__":
    main()