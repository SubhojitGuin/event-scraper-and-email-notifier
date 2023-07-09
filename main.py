import os
import smtplib
import sqlite3
import ssl
import time
import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:
    def scraper(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(self, source):
        """Extract the event details from the page source"""
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
        """Send the event name to the receiver"""
        host = "smtp.gmail.com"
        port = 465

        username = "subhojitguin2004@gmail.com"
        password = os.getenv("PASSWORD")

        receiver = "subhojitguin2004@gmail.com"
        context = ssl.create_default_context()

        message = f"""\
Subject: New Event Found!

Hey! a new event was found.
{message}
"""

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)


class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)

    def store(self, extracted):
        """Stores the new event"""
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def read(self, extracted):
        """Reads the file"""
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM events WHERE band=? AND city=? AND date=?",
            (band, city, date))
        rows = cursor.fetchall()
        return rows


if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scraper(URL)
        extracted = event.extract(scraped)
        if extracted != "No upcoming tours":
            database = Database(database_path="data.db")
            row = database.read(extracted)
            if not row:
                email = Email()
                email.send(extracted)
                database.store(extracted)
        time.sleep(2)
