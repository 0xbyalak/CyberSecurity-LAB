## Analisis Tool Brute Force

Tool ini memanfaatkan fitur XML-RPC WordPress yang memungkinkan remote procedure call (RPC) untuk berbagai fungsi, termasuk autentikasi pengguna. Fungsi `wp.getUsersBlogs` biasanya mengembalikan informasi blog yang dimiliki pengguna jika username dan password benar.

**Cara kerja utama:**

- Membuat payload XML yang berisi username dan password.
- Mengirimkan request POST ke URL `xmlrpc.php` dengan payload tersebut.
- Mengecek respons apakah mengandung tag `<name>isAdmin</name>`, yang menandakan login berhasil.
- Jika berhasil, tool mencetak username dan password yang valid dan menghentikan proses.
- Jika gagal, tool melanjutkan mencoba password berikutnya dari wordlist.
- Ada jeda 0.2 detik antar percobaan untuk menghindari flooding terlalu cepat.

**Kelebihan:**

- Sederhana dan mudah dimodifikasi.
- Menggunakan XML-RPC yang sering diaktifkan di WordPress.
- Mendukung custom User-Agent.

**Kekurangan:**

- Tidak menangani proteksi rate limiting atau mekanisme keamanan lain seperti CAPTCHA.
- Tidak mendukung multiple username secara langsung.
- Tidak ada fitur logging hasil ke file.
- Tidak ada opsi untuk melanjutkan dari titik tertentu jika proses terhenti.

## Dokumentasi Tool

### Deskripsi
Tool ini melakukan brute force login pada endpoint `xmlrpc.php` WordPress menggunakan metode XML-RPC `wp.getUsersBlogs`. Tool mencoba password dari wordlist untuk username tertentu dan melaporkan jika berhasil login.

### Persyaratan
- Python 3.x
- Modul `requests` (install dengan `pip install requests`)

### Parameter

- `-u` atau `--url`: URL target lengkap ke `xmlrpc.php`, misalnya `https://example.com/xmlrpc.php`.
- `-U` atau `--user`: Username WordPress yang akan diuji.
- `-w` atau `--wordlist`: Path ke file wordlist berisi daftar password.
- `-a` atau `--agent`: (Opsional) User-Agent HTTP yang digunakan, default `WPForce-Test/1.0`.

### Cara Kerja
1. Membaca wordlist password.
2. Mengirim request XML-RPC untuk setiap password.
3. Mengecek respons untuk indikasi login berhasil.
4. Menghentikan proses jika ditemukan password valid.



## Cara Penggunaan

1. Pastikan Python 3 dan modul `requests` sudah terpasang:

```bash
pip install requests
```

2. Download script.
```bash
wget https://raw.githubusercontent.com/0xbyalak/CyberSecurity-LAB/main/Tools/WPLogin-bruteforce/0xbyalak.py
```

4. Siapkan wordlist password, misalnya `passwords.txt`.

5. Jalankan tool dengan perintah:

```bash
python 0xbyalak.py -u https://target.com/xmlrpc.php -U admin -w passwords.txt
```

5. Jika ingin menggunakan User-Agent khusus:

```bash
python 0xbyalak.py -u https://target.com/xmlrpc.php -U admin -w passwords.txt -a "CustomAgent/1.0"
```

6. Tool akan menampilkan hasil validasi setiap password dan berhenti jika menemukan password yang benar.
```powershell
PS C:\Users\iyhor\Desktop> python 0xbyalak.py -u http://192.168.1.12/xmlrpc.php -U admin -w password.txt
[*] Starting brute force against admin on http://192.168.1.12/xmlrpc.php
[-] Invalid: admin : 12345
[-] Invalid: admin : 2004
[-] Invalid: admin : 1234567890
[-] Invalid: admin : qwerty
[-] Invalid: admin : password
[-] Invalid: admin : qwerty123
[-] Invalid: admin : banyuwangi
[+] VALID: admin : password123
PS C:\Users\iyhor\Desktop>
```
