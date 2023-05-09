import psycopg2
import requests
import json

fazar = 'Fazar: 3.34'
zuhur = 'Zuhur: 1.02'
asr = 'Asar: 5.06'
magrib = 'Magrib: 8.39'
isha = 'Isha: 9.50'

class DB_INIT:
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'mobileapp'
        self.password = 'app1234'
        self.dbname = 'prayer_time'
        self.port = '5432'
        self.connection = None

    def init_connection(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            cursor = self.connection.cursor()
            print('database connected')
            # cursor.execute("""CREATE DATABASE if not exits prayer_time""")
            cursor.execute(
                """
                CREATE TABLE if not exists prayer_time (
                    fazar TEXT,
                    zuhur TEXT,
                    asr TEXT,
                    magrib TEXT,
                    isha TEXT
                )
                """
            )
            self.connection.commit()
            self.connection.close()
        except Exception as e:
            print(e)

    def submit(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO prayer_time (fazar, zuhur, asr, magrib, isha) VALUES (%s, %s, %s, %s, %s)", (fazar, zuhur, asr, magrib, isha))

            self.connection.commit()
            self.connection.close()
        except Exception as e:
            print(e)

    def show_records(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM prayer_time")
            records = cursor.fetchall()
            self.connection.commit()
            self.connection.close()
            return records
        except Exception as e:
            print(e)

    def close_connection(self):
        try:
            self.connection.close()
            print('database treminated')

        except Exception as e:
            print(e)
