import math

def hitung_luas(jari_jari):
    return math.pi * (jari_jari ** 2)

def hitung_keliling(jari_jari):
    return 2 * math.pi * jari_jari

def main():
    try:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        if jari_jari < 0:
            print("Jari-jari tidak boleh negatif.")
            return
        
        luas = hitung_luas(jari_jari)
        keliling = hitung_keliling(jari_jari)

        print(f"Luas lingkaran: {luas:.2f}")
        print(f"Keliling lingkaran: {keliling:.2f}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()