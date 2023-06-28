

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
query = "SELECT nim FROM users"
cursor.execute(query)
results = cursor.fetchall()

# Menutup kursor dan koneksi ke database
cursor.close()
mydb.close()

# Mengirim data ke server menggunakan curl
url = 'http://10.0.0.20:8080/api/add_unix_user/'
for nim in results:
    data = f'nim={nim}&password={nim}'
    command = f'curl -X POST --data-urlencode "{data}" {url}'
    print(f"URL yang digunakan: {url}")
    print(f"Perintah curl yang dihasilkan: {' '.join(command)}")
    try:
        subprocess.run(command, shell=True, check=True)
        print("Data berhasil dikirim")
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat mengirim data: {e}")

# # Koneksi ke database MySQL
# mydb = mysql.connector.connect(
#   host="127.0.0.1",
#   user="root",
#   password="",
#   database="repository"
# )

# # Membuat kursor untuk mengeksekusi perintah SQL
# cursor = mydb.cursor()

# # Mendapatkan data NIM dan password dari tabel pengguna
# query = "SELECT nim, password FROM users"
# cursor.execute(query)
# results = cursor.fetchall()

# # Menutup kursor dan koneksi ke database
# cursor.close()
# mydb.close()

# # Mengirim data ke server
# url = 'http://127.0.0.1:8080/api/add_unix_user/'
# for nim, password in results:
#     payload = {'nim': nim, 'password': password}
#     response = requests.post(url, data=payload)
#     # Memproses tanggapan dari server
#     if response.status_code == 200:
#         print("Data berhasil dikirim")
#     else:
#         print("Terjadi kesalahan saat mengirim data")


# def connect_to_database_and_run_curl():
#     try:
#         # Menghubungkan ke database
#         cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='repository')
#         cursor = cnx.cursor()

#         # Mendapatkan data username dan password dari database
#         cursor.execute("SELECT nim, password FROM users")
#         users = cursor.fetchall()

#         # Menjalankan permintaan POST untuk setiap user
#         for user in users:
#             nim, password = user
#             # print("nim:", nim)
#             # print("password:", password)

#             url = 'http://127.0.0.1:8080/api/add_unix_user/'

#             if nim is not None and password is not None:
#                 payload = {'password': password, 'nim': nim}
#                 headers = {'Content-Type': 'application/json'}
                
#                 try:
#                     # Mengirim permintaan POST menggunakan library requests
#                     response = requests.post(url, data=json.dumps(payload), headers=headers)

#                     if response.status_code == 200:
#                         data = response.json()

#                         if data is not None:
#                             # Menggunakan pesan respons untuk tindakan lanjutan
#                             message = f"Received response from API for user '{nim}': {data}"
#                             print(message)
#                             # Lakukan tindakan lain yang diperlukan berdasarkan pesan respons
#                         else:
#                             print(f"Failed to get API response for user '{nim}'.")
#                     else:
#                         print(f"Failed to make API request for user '{nim}'. Status code: {response.status_code}")
#                 except requests.exceptions.RequestException as e:
#                     print(f"Error making API request: {e}")
#             else:
#                 print(f"Invalid nim or password for user '{nim}'")

#         # Menutup koneksi ke database
#         cursor.close()
#         cnx.close()
#     except mysql.connector.Error as err:
#         print(f"An error occurred while connecting to the database: {err}")

# # Panggil fungsi untuk terhubung ke database dan menjalankan permintaan POST
# connect_to_database_and_run_curl()



# def create_unix_user(userPass, userId):
#     url = 'http://10.0.0.20:8080/api/add_unix_user/'
#     payload = {'userPass': userPass, 'userId': userId}
#     response = requests.post(url, data=payload)
#     data = response.json()
#     return data

# userPass = "password2"
# userId = "user1234"
# result = create_unix_user(userPass, userId)
# print(result)
