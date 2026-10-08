Nama:Satria Aji Sastra
Nim:2609116019
Kelas:A

*Penjelasan Prgoram*

<img width="184" height="62" alt="Screenshot 2026-10-08 075733" src="https://github.com/user-attachments/assets/ae836c06-89a8-4075-aebc-3a3bfaed505e" />

import json: ini adalah program untuk memproses pembacaan dan penyimpanan data dalam format JSON (json.load dan json.dump).

import os: ini adalh program untuk mengecek ketersediaan file penyimpanan (os.path.exists) agar program tidak error saat pertama kali dijalankan.


<img width="516" height="94" alt="Screenshot 2026-10-08 075745" src="https://github.com/user-attachments/assets/300ec530-9a20-4633-8122-60ed5e3649e1" />

ini adalah program untuk memberikan nama file untuk nyimpan data file

<img width="742" height="258" alt="Screenshot 2026-10-08 075756" src="https://github.com/user-attachments/assets/a37c8716-4971-4fb6-a63e-07e72ad6a670" />

ini adalah program untuk membaca data yang ada di file inventaris.json.

saat file belum ada (pertama kali dijalankan), fungsi ini akan mengembalikan list kosong [] biar program tetap berjalan normal.

<img width="726" height="104" alt="Screenshot 2026-10-08 075807" src="https://github.com/user-attachments/assets/9b73f6a3-0503-4df8-ac29-b495d847a80c" />

ini adalah program untuk menulis ulang data terbaru ke file inventaris.json.

<img width="743" height="359" alt="Screenshot 2026-10-08 075818" src="https://github.com/user-attachments/assets/78f051b8-9c80-4ed2-9695-7f333eb21203" />

ini adalah program untuk melooping dan mencetak seluruh data inventaris ke terminal dalam bentuk tabel rapi menggunakan string formatting.

<img width="750" height="138" alt="Screenshot 2026-10-08 080009" src="https://github.com/user-attachments/assets/0ae3695d-3f79-4ca6-9817-96a965ab9e59" />
<img width="831" height="754" alt="Screenshot 2026-10-08 075919" src="https://github.com/user-attachments/assets/708f9c48-9c5a-4117-a7a7-dfcc1abd184b" />

ini adalah program untuk menerima input dari pengguna (ID, Nama, Jumlah, dan Harga).
Melakukan validasi sederhana untuk memastikan jumlah dan harga berupa angka (ValueError).
Memasukkan data baru ke dalam list menggunakan method .append() lalu memanggil simpan_data() agar tersimpan secara permanen.

<img width="808" height="680" alt="Screenshot 2026-10-08 080022" src="https://github.com/user-attachments/assets/e88f611e-924e-424b-aaae-638c9d03f647" />

ini adalah program untuk menu utama interaktif yang berjalan terus-menerus sampai pengguna memilih opsi keluar


*Penjelasan Output*

<img width="734" height="827" alt="Screenshot 2026-10-08 080230" src="https://github.com/user-attachments/assets/cff3da14-cbbd-4c44-a94f-145f8faa8d66" />

ini adalah output pertama dan saya memilih menu ke 2 untuk input data barang dahulu karena belum ada data barang yang dimasukkan ke program

<img width="673" height="476" alt="Screenshot 2026-10-08 080253" src="https://github.com/user-attachments/assets/f97f1d12-98d5-4d6d-b8dd-5cef23ecfff0" />

ini adalah output menu 1 yang menamplkan daftar barang

<img width="712" height="661" alt="Screenshot 2026-10-08 080343" src="https://github.com/user-attachments/assets/be9c0796-f7a1-46a6-84ff-cce89d7ba8da" />

ini adalah menu ke 3 untuk keluar program dan setelah keluar saya coba run program lagi lalu lihat daftar barang di menu 1, dan program masih tersimpan setelah keluar dari program

