import requests

from settings import config


def send_telegram(message: str):
    """ Send a Telegram message to a bot
    first a telegram bot must be created
    https://www.giga.de/apps/telegram/tipps/telegram-bot-erstellen-loeschen-andere-befehle-so-geht-s/
    """

    bot_token = config.get("telegram", "bot_token")
    bot_chat_id = config.get("telegram", "bot_chat_id")

    send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={message}"
    response = requests.get(send_text)

    return response.json()
