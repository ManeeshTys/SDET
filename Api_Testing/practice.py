import requests
import json

from payLoad import AddBook, BuildPayLoadFromDB
from utils.configuration import getConfig
from utils.resources import ApiResources
# # with open('example.json') as f:
# #     content=json.load(f)
# #     #print(content)

# response=requests.get('http://216.10.245.166/Library/GetBook.php',allow_redirects=False,params={'AuthorName':'Rahul Shetty2'})
# json_repsone = response.json()
# #print(json_repsone)
# print(type(json_repsone))
# print(response.history)
# # print(json_repsone[0]['isbn'])
from utils.configuration import getConfig


url = getConfig()["API"]["ENDPOINT"]+ApiResources.AddBook
header = {"Content-Type" : "application/json"}
query = 'select * from CustomerInfo'
addbook = requests.post(url,json=AddBook("query"),headers=header)
print(addbook.json())
respons = addbook.json()
print(type(respons))
# print(respons['ID'])
book_id = respons['ID']
print(book_id)

url = getConfig()["API"]["ENDPOINT"]+ApiResources.DeleteBook
header = {"Content-Type" : "application/json"}
deletebook = requests.post(url,json={"ID" : book_id} , headers=header)
assert deletebook.status_code == 200
res_json = deletebook.json()
print(res_json['msg'])

# # #Authentication
# se = requests.session()
# se.auth = auth = ('ManeeshTys','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')
# url='https://api.github.com/user'
# r = requests.get(url, auth=('ManeeshTys','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'))
# print(r.history)
# print(r.status_code)

# url1='https://api.github.com/user/repos'
# response = se.get(url1)
# response.json()
# print(response.status_code)

# se = requests.session()
# se.cookies.update({'visit':'jan'})
# url = 'https://httpbin.org/cookies'
# re = se.get(url,cookies={})
# print(re.history)
# #print(re.text)

# cookie = {'visit':'june'}
# res = requests.get('http://rahulshettyacademy.com',allow_redirects=True,cookies=cookie)
# print(res.history)
# print(res.status_code)

# #attachments
# url3 = 'https://petstore.swagger.io/v2/pet/984321/uploadImage'
# files = {'file':open('C:/Users/gmaneesh.PKRMSEZDC/Pictures/Screenshots/ss.png', 'rb')}
# r = requests.post(url3,files=files)
# print(r.status_code)
# print(r.text)

# print(list[reversed(i for i in range(1,11))])
# num = [1,2,3,4,5]
# num.remove(2)
# print(5!=6)
# z='s;p;k'
# print(len(z.split(';')))

# num = [1,2,3,4,5]
# print(num[-2])