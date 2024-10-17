import json
import os

# Nama file untuk menyimpan data akun
FILENAME = "accounts.json"

# Fungsi untuk memuat akun dari file
def load_accounts():
    if os.path.exists(FILENAME):  # Memeriksa apakah file ada
        try:
            with open(FILENAME, "r") as file:
                data = file.read()
                if data:  # Memastikan file tidak kosong
                    return json.loads(data)
                else:
                    return {}  # Jika file kosong, kembalikan dictionary kosong
        except json.JSONDecodeError:  # Menangani error jika file tidak berformat JSON
            print("File JSON tidak valid. Memulai dengan data akun kosong.")
            return {}
    else:
        return {}  # Jika file tidak ada, kembalikan dictionary kosong

# Fungsi untuk menyimpan akun ke file
def save_accounts():
    with open(FILENAME, "w") as file:
        json.dump(accounts, file)

# Memuat akun yang sudah ada dari file
accounts = load_accounts()

def register():
    print("=== Register Page ===")
    # Meminta user memasukkan username dan password baru
    username = input("Masukkan username baru: ")
    
    # Memastikan username belum ada di database
    if username in accounts:
        print("Username sudah terdaftar. Coba username lain.")
    else:
        password = input("Masukkan password baru: ")
        accounts[username] = password
        print(f"Registrasi berhasil! Anda sekarang dapat login sebagai {username}.")

def login():
    print("=== Login Page ===")
    
    # Meminta user memasukkan username dan password
    username = input("Username: ")
    password = input("Password: ")

    # Mengecek apakah username dan password sesuai
    if username in accounts and accounts[username] == password:
        print(f"Selamat datang, {username}!")
    else:
        print("Username atau password salah.")

def main():
    while True:
        print("\n=== Selamat datang! ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            login()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            save_accounts()  # Menyimpan akun ke file sebelum keluar
            print("Akun telah disimpan. Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Memulai program
if __name__ == "__main__":
    main()
