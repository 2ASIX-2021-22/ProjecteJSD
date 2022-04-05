import requests

def bot_send_text(bot_message):
    
    bot_token = '5118212136:AAHqt6Dm9IcmqBumezST9NWatw8W6OL-neA'
    bot_chatID = '878393620'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response
