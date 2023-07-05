

import requests

import subprocess
import mysql.connector
import shlex

# Koneksi ke database MySQL
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="meliska",
  password="meliska",
  database="repository"
)

# Membuat kursor untuk mengeksekusi perintah SQL
cursor = mydb.cursor()

# Mendapatkan data NIM dan password dari tabel pengguna
query = "SELECT id, nim FROM users"
cursor.execute(query)
results = cursor.fetchall()

# Menutup kursor dan koneksi ke database
cursor.close()
mydb.close()

# Mengirim data ke server menggunakan curl
url = 'http://10.0.0.20:8080/api/add_unix_user/'
for id, nim in results:
    data = f'nim={nim}'
    command = f'curl -X POST --data-urlencode "{data}" {url}'
    print(f"URL yang digunakan: {url}")
    print(f"Perintah curl yang dihasilkan: {' '.join(command)}")
    try:
        subprocess.run(command, shell=True, check=True)
        print("Data berhasil dikirim")
        # Update 'terdaftar' attribute in the database to 1
        update_query = "UPDATE users SET terdaftar = 1 WHERE id = %s"
        cursor.execute(update_query, (id,))
        mydb.commit()
        print("Data berhasil diperbarui")
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat mengirim data: {e}")
