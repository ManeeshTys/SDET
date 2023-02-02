from utils.configuration import getQuery


def AddBook(value1,value2):
    book = {"name":"Learn Appium Automation with Java",
            "isbn":value1,
            "aisle":value2,
            "author":"John foe"}
    return book

#print (AddBook("strew"))

def BuildPayLoadFromDB(query):
    addbody = {}
    tp = getQuery(query)
    addbody['name']= tp[0]
    addbody['isbn'] = tp[1]
    addbody['aisle'] = tp[2]
    addbody['author'] = tp[3]

    return addbody
