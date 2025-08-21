#iteration over the list
myFavoriteMobil = ["Toyota","Tesla","Bmw","Nissan"]


no = 0
for d in myFavoriteMobil:
    print("{}. {}".format(no, d))
    no = no+1
    
    
for en, d in enumerate(myFavoriteMobil):
    print(("{}. {}".format(en+1,)))
    
    
    
    
#iteration over the dict
myDict = {
    "nama": "adam",
    "asal": "batam"
    
}


print(myDict)
    
#using keys  
for key in myDict.keys():
    print(myDict[key])
    
    
# using values
for val in myDict.values():
    print("the values", val)

#using members pair
for key, val in myDict.items():
    print(key + " : " + val)