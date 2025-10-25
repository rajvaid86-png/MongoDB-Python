import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
# print(client)
db=client['student']
collection=db['courses']
# d=[
#  {"name": "Ram", "course": "Data Science", "Reg_fee": 1000, "c_fee": 48000},
#   {"name": "Shyam", "course": "Web Development", "Reg_fee": 800, "c_fee": 35000},
#   {"name": "Priya", "course": "Artificial Intelligence", "Reg_fee": 1200, "c_fee": 60000},
#   {"name": "Aman", "course": "Cyber Security", "Reg_fee": 900, "c_fee": 40000},
#   {"name": "Sneha", "course": "Data Science", "Reg_fee": 1100, "c_fee": 55000},
#   {"name": "Ravi", "course": "Full Stack Development", "Reg_fee": 950, "c_fee": 45000},
#   {"name": "Kiran", "course": "Data Science", "Reg_fee": 1000, "c_fee": 50000},
#   {"name": "Neha", "course": "UI/UX Design", "Reg_fee": 750, "c_fee": 30000},
#   {"name": "Arjun", "course": "Blockchain", "Reg_fee": 1300, "c_fee": 65000},
#   {"name": "Meera", "course": "Data Analytics", "Reg_fee": 1000, "c_fee": 47000}
# ]

# collection.insert_many(d) 

# pipeline = [
#   {
#     "$match": { "course": "Data Science" }
#   }
# ]

# document = collection.aggregate(pipeline)

# for doc in document:
#     print(doc)



pipeline = [
    {
        "$match":{"course":"Data Science"}
    },
    {
        "$group":{
            "_id":"course",
            "total_students":{"$sum":1},
            "avg_fee":{"$avg":"$c_fee"}
        }
    },
    {
        "$sort":{"total_students":-1}
    }
]

result=collection.aggregate(pipeline)

for i in result:
    print(i)