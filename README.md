# Sistem Data Mahasiswa — UTS Pemrograman Berorientasi Objek

Program sederhana berbasis terminal menggunakan Python dan konsep Object-Oriented Programming (OOP).

## Fitur
- Menambahkan data mahasiswa.
- Menampilkan seluruh data mahasiswa.
- Mencari mahasiswa berdasarkan NIM.
- Mengubah nilai mahasiswa.
- Menghapus data mahasiswa.
- Menampilkan jumlah object mahasiswa yang pernah dibuat.
- Validasi NIM, nama, dan nilai.

## Cara menjalankan
1. Pastikan Python sudah terpasang.
2. Buka terminal pada folder project.
3. Jalankan perintah:

   ```bash
   python main.py
   ```

## Penerapan konsep OOP

| Konsep | Penerapan dalam program |
|---|---|
| Class | `Mahasiswa` dan `SistemDataMahasiswa` |
| Object | Object dibuat dari class `Mahasiswa` dan `SistemDataMahasiswa` |
| Constructor | `__init__()` pada kedua class |
| Attribute | NIM, nama, nilai, dan daftar mahasiswa |
| Method | `tambah_mahasiswa()`, `cari_mahasiswa()`, `ubah_nilai()`, dan lainnya |
| Encapsulation | Attribute `__nim`, `__nama`, `__nilai`, dan `__daftar_mahasiswa` dibuat private |
| Property/setter | `@property` dan `@nama.setter` untuk NIM, nama, dan nilai |
| Class method | `@classmethod jumlah_dibuat()` untuk membaca jumlah object mahasiswa yang dibuat |
| Static method | `@staticmethod validasi_nim()` untuk memeriksa format NIM |
| Special method | `__str__()` untuk mengatur tampilan object saat dicetak |

## Catatan
Data disimpan sementara di dalam list selama program berjalan. Data akan kembali kosong ketika program ditutup karena tugas ini tidak mewajibkan database.
