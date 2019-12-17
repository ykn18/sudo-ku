import pymongo
import os

client = pymongo.MongoClient('mongo:27017', username='root', password='toor', authSource='admin')

db = client['authentication_db']
if 'servers' in db.list_collection_names():
    print('Migration already updated')
else:
    collection = db['servers'] 
    servers = [
        {'servername':'gameserver','password':'$2y$12$Ik3X.4qSaWSuDCUtDOBNe.w.HlAupvDPENB3PNMQsThA6TA652tM.'},
        {'servername':'generatorserver','password':'$2y$12$Hfc/Pr3EjzPXLlED1MOHn./cTtiWkO.J8U6P9LHCOF3Um2yxTZ.HC'},
        {'servername':'statisticserver','password':'$2y$12$1MvGXK73dHvzXCU47AzaO.C9G5gc5Esnclr.XSlOb6pxPkt3Ay4sq'}
    ]

    res = collection.insert_many(servers)
    print(res.inserted_ids)