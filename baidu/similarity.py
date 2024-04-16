from aip import AipNlp

with open('key.txt') as f:
    info = f.read().split('\n')

APP_ID = info[2]
API_KEY = info[3]
SECRET_KEY = info[4]

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def similarity(text1, text2):
  return client.simnet(text1, text2)
