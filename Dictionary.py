# store data in key and value

dict = {

    "Name" : "Samriddhi Shukla",
    "Age" : 20,
    "Language" : "Python"
}
print(dict)

#It is unordered,mutable and don't allow duplicate keys
print(dict["Name"])
dict["Name"] = "Naam"
dict["Surname"] = "Shukla"
print(dict)

#nested dictionary


Girl = {
    "Name" : "Samridhi Shukla",
    "Age" : 20,
    "Hobbies" : {
        "1" : "Cooking",
        "2" : "Coding",
        "3" : "Singing",
        "4" : "Meditation"
    }
}
print(Girl)

print(Girl.keys())
print(len(Girl))
print(dict.values())

d = {
    "cat" : "a small animal",
    "table" : ["a piece of fun","lof"]

}
print(d)





