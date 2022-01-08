import requests

bot_token = 'example'  #Insert your own token here
bot_chatID = 'example' #Insert your own ID here

class NotificationManager:

    def __init__(self):
        pass

    def send_message(self, message):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
                    + bot_chatID + '&parse_mode=Markdown&text=' + message
        response = requests.get(send_text)
        # Prints if successfully sent.
        print(message)
    
