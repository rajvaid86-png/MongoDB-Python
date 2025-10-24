import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

db=client['school']

collection=db['result']

                                    # CREAT

# collection.insert_one({"name":"Raj","age":21,"grade":"A"})

# students=[
#     {"name":"Aman","age":20,"grade":"C"},
#     {"name":"Harsh","age":23,"grade":"B"},
#     {"name":"Laksh","age":21,"grade":"B"}
# ]


# collection.insert_many(students)


                                #  READ(find)

# result=collection.find_one({"name":"Raj"})
# print(result)


# for i in collection.find({"grade":"B"}):
#     print(i)

for i in collection.find():
    print(i)


                    # UPDATE

# collection.update_one({"name":"Raj"},{"$set":{"grade":"A+"}})

# collection.update_many({"garde":"B"},{"$set":{"grade":"A"}})


                        # DELETE


# collection.delete_one({"name":"Raj"})

# collection.delete_many({"grade":"B"})