from time import sleep

from datetime import datetime, time

from crawler import WebsiteCrawler
from helpers import convert_string_to_time
from settings import config
from telegram_bot import send_telegram

interval_minutes = config.getint("general", "interval_minutes")

send_live_bits = config.getboolean("general", "send_live_bits")
live_bit_only_on_weekdays = [1, 2, 3, 4, 5, 6, 7]

raw_start_time = config.get("general", "start_time")

start_time = convert_string_to_time(config.get("general", "start_time"))
end_time = convert_string_to_time(config.get("general", "end_time"))

if __name__ == '__main__':
    crawler = WebsiteCrawler()

    send_telegram("Service gestartet")

    previous_day = -1
    while True:

        try:
            now_time = datetime.now().time()

            # check website between this time
            if start_time <= now_time <= end_time:
                crawler.compare()

                if send_live_bits \
                        and datetime.now().isoweekday() != previous_day \
                        and datetime.now().isoweekday() in live_bit_only_on_weekdays:
                    previous_day = datetime.now().isoweekday()
                    send_telegram(
                        f"Starte Überprüfung des Corona Ergebnisses alle {interval_minutes} Minuten im Zeitraum von {start_time} bis {end_time}")

            sleep(interval_minutes * 60)

        except Exception as e:
            send_telegram(f"WebsiteCrawler Error: {e} \nDas Programm wird beendet")
            exit()
