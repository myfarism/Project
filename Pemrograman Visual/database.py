import mysql.connector
from mysql.connector import Error
from datetime import datetime

class Database:
    # Static variables to store database details
    host = ''
    database = ''
    user = ''
    password = ''
    port = ''
    auth_plugin = ''

    @staticmethod
    def check_credentials(username, password):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM users WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()
                cursor.close()
                connection.close()
                if user:
                    return user['tipe_akun']
                else:
                    return False
        except Error as e:
            print("Error while connecting to MySQL", e)
            return False

    @staticmethod
    def register(username, password, name):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                # Check if username already exists
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                existing_user = cursor.fetchone()
                if existing_user:
                    return False
                else:
                    # If username does not exist, perform registration
                    query = "INSERT INTO users (username, password, nama, tipe_akun) VALUES (%s, %s, %s, 'user')"
                    cursor.execute(query, (username, password, name))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return True
        except Error as e:
            print("Error while connecting to MySQL", e)
            return False
        
    @staticmethod
    def get_laptops():
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT * FROM list_laptop"
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                connection.close()
                return data
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
        
    @staticmethod
    def add_laptop(kode_laptop, jenis_laptop, harga_sewa):
        # Tambahkan laptop ke database
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO list_laptop (kode_laptop, jenis_laptop, harga_sewa) VALUES (%s, %s, %s)"
                cursor.execute(query, (kode_laptop, jenis_laptop, harga_sewa))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False
    
    @staticmethod
    def delete_laptop(kode_laptop):
        # Hapus laptop dari database
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "DELETE FROM list_laptop WHERE kode_laptop = %s"
                cursor.execute(query, (kode_laptop,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False
        
    @staticmethod
    def get_kode():
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT kode_laptop FROM list_laptop WHERE status IS NULL"
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                connection.close()
                return data
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
        
    @staticmethod
    def get_jenis(selected_kode):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                # Construct SQL query to select laptop type based on selected code
                query = "SELECT jenis_laptop FROM list_laptop WHERE kode_laptop = %s"
                cursor.execute(query, (selected_kode,))
                laptop_type = cursor.fetchone()[0]  # Fetch the first row and extract laptop type
                cursor.close()
                connection.close()
                return laptop_type
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
        
    @staticmethod
    def get_harga(selected_kode):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                # Construct SQL query to select laptop type based on selected code
                query = "SELECT harga_sewa FROM list_laptop WHERE kode_laptop = %s"
                cursor.execute(query, (selected_kode,))
                harga_sewa = cursor.fetchone()[0]  # Fetch the first row and extract laptop type
                cursor.close()
                connection.close()
                harga_sewa = float(harga_sewa)
                return harga_sewa
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
    
    @staticmethod
    def get_list():
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                # Construct SQL query to select laptop type based on selected code
                query = "SELECT id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at FROM sewa_laptop WHERE jam_akhir is null"
                cursor.execute(query)
                data = cursor.fetchall()  # Fetch the first row and extract laptop type
                cursor.close()
                connection.close()
                return data
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
    
    @staticmethod
    def sewa_laptop(kode_laptop, jenis_laptop, harga_sewa, username):
        now = datetime.now()
        time = now.strftime("%H:%M:%S") 
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO sewa_laptop(kode_laptop, jenis_laptop, harga_sewa, jam_mulai, user) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (kode_laptop, jenis_laptop, harga_sewa, time, username))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False

    @staticmethod
    def akhiri_sewa(id_sewa):
        now = datetime.now()
        time = now.strftime("%H:%M:%S") 
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                # Ambil waktu mulai sewa
                query_mulai = "SELECT jam_mulai FROM sewa_laptop WHERE id_sewa = %s AND jam_akhir IS NULL"
                cursor.execute(query_mulai, (id_sewa,))
                jam_mulai = cursor.fetchone()[0]

                # Perbarui jam akhir sewa
                update_query = "UPDATE sewa_laptop SET jam_akhir = %s WHERE id_sewa = %s AND jam_akhir IS NULL"
                cursor.execute(update_query, (time, id_sewa))
                connection.commit()

                # Ambil nilai jam_akhir dari data terakhir yang dimasukkan ke dalam tabel sewa_laptop
                query_akhir = "SELECT jam_akhir FROM sewa_laptop WHERE id_sewa = %s ORDER BY created_at DESC LIMIT 1"
                cursor.execute(query_akhir, (id_sewa,))
                jam_akhir = cursor.fetchone()[0]

                cursor.close()
                connection.close()
                jam_mulai = str(jam_mulai)
                jam_akhir = str(jam_akhir)
                return jam_mulai, jam_akhir  # Kembalikan waktu mulai dan waktu akhir sewa
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None, None
        
    @staticmethod
    def update_harga(total_harga, id_sewa):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                update_query = "UPDATE sewa_laptop SET total_harga = %s WHERE sewa_laptop.id_sewa = %s"
                cursor.execute(update_query, (total_harga, id_sewa))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False
    
    @staticmethod
    def riwayat(username):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                # Construct SQL query to select laptop type based on selected code
                query = "SELECT * FROM sewa_laptop WHERE jam_akhir IS NOT NULL AND user = %s"
                cursor.execute(query, (username,))
                data = cursor.fetchall()  # Fetch the first row and extract laptop type
                cursor.close()
                connection.close()
                return data
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
        
    @staticmethod
    def update_status_aktif(kode_laptop):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                update_query = "UPDATE list_laptop SET status = 'aktif' WHERE kode_laptop = %s "
                cursor.execute(update_query, (kode_laptop,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False
        
    @staticmethod
    def update_status_null(kode_laptop):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 port=Database.port,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password,
                                                 auth_plugin=Database.auth_plugin)
            if connection.is_connected():
                cursor = connection.cursor()
                update_query = "UPDATE list_laptop SET status = NULL WHERE kode_laptop = %s "
                cursor.execute(update_query, (kode_laptop,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False
