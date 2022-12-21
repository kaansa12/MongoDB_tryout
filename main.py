
#Created By: Kaan Kalkan @ER-FA at 12/21/2022
# YouTube Video MongoDB Crash Course With Python 2022 By Patrick Loeber
# https://www.youtube.com/watch?v=qWYx5neOh2s
# MANUEL DB OPERATORS https://www.mongodb.com/docs/manual/reference/operator/
#pip install pymongo

import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
import datetime
cluster = "mongodb+srv://KaanKalkan:<password>@newmongoproject.gshwhde.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)

db = client.MytestDB #ya yeni db ekle yada zaten olan dbyi kullan
MyCollection = db.MyCollection # new_something i bir collection oluşturuyor
#MyElement = {"name": "Kaan", "text": "sa bitches", "status": "open",
        #"tags": ["python", "coding"] , "date": datetime.datetime.utcnow()}

#MyCollection.insert_one(MyElement) # res = a.i_o(b) a collectionunun içine b elementini atıyor
def LeaveSpace():
    print("-----------------------------------------------------")

def OutResults(ResList):
    for i in ResList: #işte içindekileri bulmak için
        print(i)

def Mongo():



    MyElements = \
    [{"name": "Kaan", "text": "Hello", "status": "open",
    "tags": ["English", "Got drunk from tea", "Bloody hell mate"] , "date": datetime.datetime.utcnow()},
    {"name": "KaanV2", "text": "Hallo", "status": "Wie geht's ? ",
    "tags": ["German", "Frankfurter Wurst","Prost!"] , "date": datetime.datetime.utcnow()},
    {"name": "KaanV3", "text": "Salut", "status": "Fuck off",
    "tags": ["French", "Don't come near", "You bastard"] , "date": datetime.datetime.utcnow()},
    {"name": "KaanV4", "text": "Priviet", "status": "none of your bussiness",
    "tags": ["Russian", "Vodka", "Yum Yum Vodka"] , "date": datetime.datetime.utcnow()}] # şu tek \ bu satırda kodu kesme demek heralde

    MyCollection.insert_many(MyElements)

    print(client.list_database_names())# dblerin adını gösteriyor
    print(db.list_collection_names())# dblerin içlerindeki listeleri gösteriyor


def Mongo2():
    print(MyCollection.find_one({"name": "KaanV2"}))
    print(MyCollection.find_one({"_id": ObjectId("63a2fb2ef973730177a456d9")}))

    LeaveSpace()

    results = MyCollection.find()
    results2 = MyCollection.find({"tags": "Vodka"})

    OutResults(results)

    LeaveSpace()

    OutResults(results2)

    LeaveSpace()

    print(MyCollection.count_documents({})) # içinde kaç tane element olduğunu bulmak için
    LeaveSpace()
    print(MyCollection.count_documents({"tags": "Vodka"}))
    LeaveSpace()

    d = datetime.datetime(2022,12,31)

    results3 = MyCollection.find({"date": {"$lt": d}}).sort("text") #text e göre düzenliyoruz
    # $lt "less than" $gt de "greater than"  demek yani
    # burda da var geri kalanlar https://www.mongodb.com/docs/manual/reference/operator/query/
    # belirlediğimiz tarihten az tarihte olanları alcaz

    OutResults(results3)

    LeaveSpace()

    # MyCollection.delete_one({"name": "KaanV3"}) kaanV3ü sildim :D
    results = MyCollection.find()

    OutResults(results) #işte içindekileri bulmak için
    #not: nedense results u üste kullanmıştım bida kullanmayı deneyince boş verdi
    #ama results u bida tanımlıyınca oldu nedeni bilinmiyor hata vsde yok
    #dikkat yani ok
    LeaveSpace()
    #MyCollection.delete_many({"tags": "Vodka"}) # Vodka taglileri sildim :D

    results = MyCollection.find()

    OutResults(results)

def Mongo3():
    MyCollection.update_one({"name": "Kaan"}, {"$set": {"status": "Died from tea"}})
    # 1 tane elementi updateledim
    MyCollection.update_one({"name": "Kaan"}, {"$unset": {"date": None}})#datei çıkardım şimdilik Kaandan
    # geri eklemek için $set kullancam yani $set olan bir eleman yoksa yerine koyuyor dediğimiz şeyi

    results = MyCollection.find()

    OutResults(results)

def Mongo4():

    MyElement = [{"name": f"TestSubject:1"}]
    """
    for i in range(2,10):

        MyElement.append({"name": f"TestSubject:{i}"})



        LeaveSpace()

    print(MyElement)
    MyCollection.insert_many(MyElement)
    print("done!")
    """
    """
    for i in range(2,1000):
        MyElement = {"name": f"TestSubject:{i}"}
        MyCollection.delete_one(MyElement)
        LeaveSpace()
        """



