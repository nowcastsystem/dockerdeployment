import pymongo
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["quantaxis"]
# print(myclient.list_database_names())

# print(mydb.list_collection_names())
quant = mydb['stock_day']
myquery = {"code": "000002"}

mydoc = quant.find(myquery)

datatest = myclient['mydatabase']
testcol = datatest['000002']
num = testcol.count()
mycol = datatest['streaming']

for i in range(num):
    que = {'_id': i + 1}
    doc = testcol.find_one(que)
    # print(doc)
    mycol.insert_one(doc)
    time.sleep(1)

if __name__ == '__main__':
    test.run(debug=True)
