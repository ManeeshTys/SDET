import requests
from behave import *
from payLoad import AddBook

from utils.configuration import getConfig
from utils.resources import ApiResources


@given('the book details which needs to be added to Library')
def step_impl(context):
    context.url = getConfig()["API"]["ENDPOINT"]+ApiResources.AddBook
    context.header = {"Content-Type" : "application/json"}
    context.PayLoad = AddBook('query25','413')

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url,json=context.PayLoad,headers=context.header)


@then('book details added successfully')
def step_impl(context):
    print(context.response.json())
    context.r = context.response.json()
    #print(respons)
    context.book_id = context.r['ID']
    print(context.book_id)
    assert context.r["Msg"] == "successfully added"

@given('the book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = getConfig()["API"]["ENDPOINT"]+ApiResources.AddBook
    context.header = {"Content-Type" : "application/json"}
    context.PayLoad = AddBook(isbn,aisle)

@given('I have github credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('ManeeshTys','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')
    
@when('I hit getRepo API gitHub')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)

@then('staus code of response should be {statusCode:d}')
def step_impl(context,statusCode):    
    print(context.response.status_code)
    assert context.response.status_code == statusCode

