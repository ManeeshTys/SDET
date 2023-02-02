import requests

from utils.configuration import getConfig
from utils.resources import ApiResources

def after_scenario(context,scenario):
    if "Library" in scenario.tags:
        url = getConfig()["API"]["ENDPOINT"]+ApiResources.DeleteBook
        header = {"Content-Type" : "application/json"}
        deletebook = requests.post(url,json={"ID" : context.book_id} , headers=header)
        assert deletebook.status_code == 200
        res_json = deletebook.json()
        print(res_json['msg'])
        assert res_json['msg'] == 'book is successfully deleted'
