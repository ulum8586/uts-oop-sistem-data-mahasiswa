class Mahasiswa:
    """Mewakili satu data mahasiswa."""

    total_dibuat = 0

    def __init__(self, nim, nama, nilai):
        # Setter dipakai agar data divalidasi saat object dibuat.
        self.nim = nim
        self.nama = nama
        self.nilai = nilai
        Mahasiswa.total_dibuat += 1

    @staticmethod
    def validasi_nim(nim):
        """NIM harus berupa angka dengan panjang 6 sampai 15 digit."""
        nim = str(nim).strip()
        return nim.isdigit() and 6 <= len(nim) <= 15

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, nim):
        nim = str(nim).strip()
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError("NIM harus berisi 6 sampai 15 digit angka.")
        self.__nim = nim

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama):
        nama = str(nama).strip()
        if not nama:
            raise ValueError("Nama tidak boleh kosong.")
        self.__nama = nama

    @property
    def nilai(self):
        return self.__nilai

    @nilai.setter
    def nilai(self, nilai):
        try:
            nilai = float(nilai)
        except (TypeError, ValueError) as exc:
            raise ValueError("Nilai harus berupa angka.") from exc

        if not 0 <= nilai <= 100:
            raise ValueError("Nilai harus berada di antara 0 sampai 100.")
        self.__nilai = nilai

    @classmethod
    def jumlah_dibuat(cls):
        """Mengembalikan jumlah object mahasiswa yang sudah dibuat."""
        return cls.total_dibuat

    def __str__(self):
        return f"NIM: {self.nim} | Nama: {self.nama} | Nilai: {self.nilai:.2f}"


class SistemDataMahasiswa:
    """Mengelola kumpulan data mahasiswa selama program berjalan."""

    def __init__(self):
        self.__daftar_mahasiswa = []

    def tambah_mahasiswa(self, nim, nama, nilai):
        nim = str(nim).strip()
        if self.cari_mahasiswa(nim) is not None:
            raise ValueError("NIM sudah terdaftar.")

        mahasiswa = Mahasiswa(nim, nama, nilai)
        self.__daftar_mahasiswa.append(mahasiswa)
        return mahasiswa

    def tampilkan_semua(self):
        return self.__daftar_mahasiswa.copy()

    def cari_mahasiswa(self, nim):
        nim = str(nim).strip()
        for mahasiswa in self.__daftar_mahasiswa:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    def ubah_nilai(self, nim, nilai_baru):
        mahasiswa = self.cari_mahasiswa(nim)
        if mahasiswa is None:
            return False

        # Assignment ke property akan menjalankan setter dan validasi.
        mahasiswa.nilai = nilai_baru
        return True

    def hapus_mahasiswa(self, nim):
        mahasiswa = self.cari_mahasiswa(nim)
        if mahasiswa is None:
            return False

        self.__daftar_mahasiswa.remove(mahasiswa)
        return True


def tampilkan_menu():
    print("\n=== SISTEM DATA MAHASISWA ===")
    print("1. Tambah mahasiswa")
    print("2. Tampilkan semua mahasiswa")
    print("3. Cari mahasiswa")
    print("4. Ubah nilai mahasiswa")
    print("5. Hapus mahasiswa")
    print("6. Lihat jumlah object mahasiswa dibuat")
    print("0. Keluar")


def main():
    sistem = SistemDataMahasiswa()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                nim = input("Masukkan NIM (6-15 digit): ")
                nama = input("Masukkan nama: ")
                nilai = input("Masukkan nilai (0-100): ")
                mahasiswa = sistem.tambah_mahasiswa(nim, nama, nilai)
                print("Data berhasil ditambahkan:", mahasiswa)

            elif pilihan == "2":
                daftar = sistem.tampilkan_semua()
                if not daftar:
                    print("Belum ada data mahasiswa.")
                else:
                    print("\n--- DAFTAR MAHASISWA ---")
                    for nomor, mahasiswa in enumerate(daftar, start=1):
                        print(f"{nomor}. {mahasiswa}")

            elif pilihan == "3":
                nim = input("Masukkan NIM yang dicari: ")
                mahasiswa = sistem.cari_mahasiswa(nim)
                if mahasiswa is None:
                    print("Mahasiswa tidak ditemukan.")
                else:
                    print("Data ditemukan:", mahasiswa)

            elif pilihan == "4":
                nim = input("Masukkan NIM mahasiswa: ")
                nilai_baru = input("Masukkan nilai baru (0-100): ")
                if sistem.ubah_nilai(nim, nilai_baru):
                    print("Nilai berhasil diperbarui.")
                else:
                    print("Mahasiswa tidak ditemukan.")

            elif pilihan == "5":
                nim = input("Masukkan NIM yang akan dihapus: ")
                if sistem.hapus_mahasiswa(nim):
                    print("Data mahasiswa berhasil dihapus.")
                else:
                    print("Mahasiswa tidak ditemukan.")

            elif pilihan == "6":
                print(
                    "Jumlah object mahasiswa yang pernah dibuat:",
                    Mahasiswa.jumlah_dibuat(),
                )

            elif pilihan == "0":
                print("Program selesai. Terima kasih.")
                break

            else:
                print("Pilihan tidak tersedia. Silakan pilih menu 0-6.")

        except ValueError as error:
            print("Input tidak valid:", error)


if __name__ == "__main__":
    main()
