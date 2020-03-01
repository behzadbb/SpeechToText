import pymongo


class MongoHelper:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    dbName = ""

    def init(self, dbAddress="mongodb://localhost:27017/", dbName="callcenter_tejarat"):
        dblist = self.myclient.list_database_names()
        if not dbName in dblist:
            self.myclient = pymongo.MongoClient(dbAddress)
            self.dbName = self.myclient[dbName]

    def createCollection(self, collactionName):
        collist = self.dbName.list_collection_names()
        if not collactionName in collist:
            return self.dbName[collactionName]

    def insertCollaction(self, collactionName, data):
        myCollection = self.createCollection(collactionName)
        myCollection.insert_one(data)