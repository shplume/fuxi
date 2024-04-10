import json

from aliyunsdkalinlp.request.v20200629 import GetWeChGeneralRequest

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException

with open('key.txt') as f:
    info = f.read().split('\n')

access_key_id = info[0]
access_key_secret = info[1]

# 创建AcsClient实例
client = AcsClient(
  access_key_id,
  access_key_secret,
  "cn-hangzhou"
)

def vector():
  request = GetWeChGeneralRequest.GetWeChGeneralRequest()
  request.set_Text("本行董事会、监事会及董事、监事、高级管理人员保证年度报告内容的真实、准确、完整，不存在虚假记载、误导性陈述或重大遗漏，并承担个别和连带的法律责任")
  request.set_Size("100")
  request.set_Type("word")
  request.set_ServiceCode("alinlp")
  request.set_Operation("none")

  try: 
    response = client.do_action_with_exception(request)
    resp_obj = json.loads(response)
    print(resp_obj)
  except Exception as e:
    print(e)
