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

# Mengirim data ke server menggunakan curl
url = 'http://10.0.0.20:8181/api/add_unix_user/'
for id, nim in results:
    data = f'nim={nim}'
    command = f'curl -X POST --data-urlencode "{data}" {url}'
    print(f"URL yang digunakan: {url}")
    print(f"Perintah curl yang dihasilkan: {' '.join(command)}")
    try:
        subprocess.run(command, shell=True, check=True)
        print("Data berhasil dikirim")
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat mengirim data: {e}")

# Menutup kursor dan koneksi ke database
cursor.close()
mydb.close()
