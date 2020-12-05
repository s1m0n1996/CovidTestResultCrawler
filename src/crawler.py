import requests

from settings import config
from telegram_bot import send_telegram


class WebsiteCrawler(object):
    def __init__(self):
        self.__url = f"https://ixpatient.com/ixshare/ticket/{config.get('website', 'ticket_id')}"

    def compare(self):

        login_data = {
            "pin": config.get("website", "pin")
        }

        session = requests.Session()

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
        }

        raw_request = session.post(self.__url, data=login_data, headers=header)
        if raw_request.status_code != 200:
            send_telegram("Fehler beim Anmelden auf der Seite des Testergebnisses. Das Programm wird beendet")
            exit()

        request = raw_request.json()
        message = str()

        try:
            message = request["results"][0]["headline"]
            message += "  Das Programm wird nun automatisch beendet."
        except:
            send_telegram("Testergebnis hat sich verändert. Das Programm wird nun automatisch beendet.")
            exit()

        if message != "Ihre Probe ist auf dem Weg ins Labor.":
            send_telegram(message)
            exit()

        return
