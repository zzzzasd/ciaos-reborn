import re
import pprint
import logging
import gspread
import requests
import io
from PIL import Image
from oauth2client.service_account import ServiceAccountCredentials
from telethon import TelegramClient


# Logging configuration
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# Telegram Configuration
telegram_api_id = 134421
telegram_api_hash = '734dc636ee3cd0ebf51421c88f4f0b9e'


# Google Spreadsheet configuration
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'python-execel-a2689c5cf845.json', scope)


# Initiate Google Spreadsheet
# gc = gspread.authorize(credentials)
# spreadsheet = gc.open_by_key('1CMBDgfSsqPH9lsMsbD3o_Giha5HTDxigHhKuuPf29Ag')
# worksheet = spreadsheet.get_worksheet(0)

# values_list = worksheet.col_values(1)
# # print(values_list)
#
# for i in range(len(values_list)):
#     if (values_list[i] != ''):
#         t = re.search(r'\w+', values_list[i])
#         print(t.group(0))


response = requests.post("https://wrapapi.com/use/ciaos/tradingview/popular/0.0.2", json={
  "wrapAPIKey": "VwSE9mD4FmbRb8O65jAyAXYthUQ9oqdc"
})
json = response.json()
image_data = requests.get(json['data']['output']['image_url'])
open('temp.png', 'wb').write(image_data.content)

# Initiate Client
client = TelegramClient('session_name', telegram_api_id, telegram_api_hash)
client.start()
#client.send_message('ascendtrading',json['data']['output']['image_url'])
client.send_file('shern720', 'temp.png', caption=json['data']['output']['desc'][:200], force_document=False)

##
# Extra features
#
# http://telethon.readthedocs.io/en/latest/
# https://github.com/LonamiWebs/Telethon/tree/master/telethon_examples
##
# client.download_profile_photo('haolun')
# messages = client.get_message_history('haolun')
# client.download_media(messages[0])
# pass
