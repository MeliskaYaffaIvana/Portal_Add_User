import requests

import json
import mysql.connector
import subprocess

# def connect_to_database_and_run_curl():
#     try:
#         # Menghubungkan ke database
#         cnx = mysql.connector.connect(user='meliska', password='meliska', host='127.0.0.1', database='repository')
#         cursor = cnx.cursor()

#         # Mendapatkan data username dan password dari database
#         cursor.execute("SELECT nim, password FROM users")
#         users = cursor.fetchall()

#         # Menjalankan perintah curl untuk setiap user
#         for user in users:
#             nim, password = user

#             url = 'http://10.0.0.20:8080/api/add_unix_user/'
#             payload = {'userPass': password, 'userId': nim}

#             # Convert payload to JSON string
#             payload_json = json.dumps(payload)

#             # Construct the curl command
#             curl_command = f"curl -X POST -d '{payload_json}' {url}"

#             try:
#                 # Execute curl command using subprocess
#                 process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#                 output, error = process.communicate()

#                 if process.returncode != 0:
#                     raise subprocess.CalledProcessError(process.returncode, curl_command, output=output, stderr=error)

#                 # Parse the response
#                 data = json.loads(output)
                
#                 if data is not None:
#                     # Menggunakan pesan respons untuk tindakan lanjutan
#                     message = f"Received response from curl for user '{nim}': {data}"
#                     print(message)
#                     # Lakukan tindakan lain yang diperlukan berdasarkan pesan respons
#                 else:
#                     print(f"Failed to get curl response for user '{nim}'.")
#             except subprocess.CalledProcessError as e:
#                 print(f"Error executing curl command: {e.output}")
#             except Exception as e:
#                 print(f"An error occurred: {e}")

#         # Menutup koneksi ke database
#         cursor.close()
#         cnx.close()
#     except mysql.connector.Error as err:
#         print(f"An error occurred while connecting to the database: {err}")

# # Panggil fungsi untuk terhubung ke database dan menjalankan perintah curl
# connect_to_database_and_run_curl()



# import requests

# import json
# import mysql.connector
# import requests

def connect_to_database_and_run_curl():
    try:
        # Menghubungkan ke database
        cnx = mysql.connector.connect(user='meliska', password='meliska', host='127.0.0.1', database='repository')
        cursor = cnx.cursor()

        # Mendapatkan data username dan password dari database
        cursor.execute("SELECT nim, password FROM users")
        users = cursor.fetchall()

        # Menjalankan permintaan POST untuk setiap user
        for user in users:
            nim, password = user

            url = 'http://127.0.0.1:8080/api/add_unix_user/'
            payload = {'userPass': password, 'userId': nim}

            try:
                # Mengirim permintaan POST menggunakan library requests
                response = requests.post(url, json=payload)

                if response.status_code == 200:
                    data = response.json()

                    if data is not None:
                        # Menggunakan pesan respons untuk tindakan lanjutan
                        message = f"Received response from API for user '{nim}': {data}"
                        print(message)
                        # Lakukan tindakan lain yang diperlukan berdasarkan pesan respons
                    else:
                        print(f"Failed to get API response for user '{nim}'.")
                else:
                    print(f"Failed to make API request for user '{nim}'. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error making API request: {e}")

        # Menutup koneksi ke database
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"An error occurred while connecting to the database: {err}")

# Panggil fungsi untuk terhubung ke database dan menjalankan permintaan POST
connect_to_database_and_run_curl()


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

