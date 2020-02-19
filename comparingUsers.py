data = []
dataItem = []
users = []
highestAge = 0
highest_tScore = 0
person = ""


# def calulateHighestAge(users,highestAge,count):
#     for element in users:
#         if element.getAge() > highestAge:
#             highestAge = element.getAge()

# class
class User:
    # constructor
    def __init__(self,fName,lName,age,pNum,email,tScore):
        self.fName = fName
        self.lName = lName
        self.age = age
        self.pNum = pNum
        self.email = email
        self.tScore = tScore
    
    # class methods
    def getfName(self):
        return self.fName

    def getlName(self):
        return self.lName
    
    def getAge(self):
        return self.age
    
    def getpNum(self):
        return self.pNum

    def getEmail(self):
        return self.email

    def gettScore(self):
        return self.tScore

    def display(self):
        return f"{self.fName}   | {self.lName}  | {self.age}    | {self.pNum}   | {self.email}    | {self.tScore}"

# opens up a file to read data
myFile = open("users.txt","r")

# gets the line
content=myFile.readlines()
for i in content:
    data.append(i)

for element in data:
    line = element.split()
    for word in line:
        dataItem.append(word)
    print(dataItem)
    users.append(User(dataItem[0],dataItem[1],int(dataItem[2]),dataItem[3],dataItem[4],int(dataItem[5])))
    dataItem.clear()

myFile.close()

# start outputing information
print("First Name   | Last Name     | Age   | Phone #   | Email     | Test Score")
print("--------------------------------------------------------------------------")

# recieves all user's info
for element in users:
    print(element.display())
    # print(f"{element.getfName()}    | {element.getlName()}  | {element.getAge()}    | {element.getpNum()}   | {element.getEmail()}  | {element.gettScore()}")
    
# getting highestAge
print("--------------------------------------------------------------------------")
for element in users:
    if element.getAge() > highestAge:
        highestAge = element.getAge()
        person = element.getfName() + " " + element.getlName()

print(f"{person} is the oldest at age: {highestAge}!")
person = ""

# getting lowestAge
lowestAge = users[0].getAge()
for element in users:
    if element.getAge() < lowestAge:
        lowestAge = element.getAge()
        person = element.getfName() + " " + element.getlName()

print(f"{person} is the youngest at age: {lowestAge}!")
person = ""

# getting highest_tScore
print("--------------------------------------------------------------------------")
for element in users:
    if element.gettScore() > highest_tScore:
        highest_tScore = element.gettScore()
        person = element.getfName() + " " + element.getlName()

print(f"{person} has the highest test score at: {highest_tScore}!")
person = ""

# getting lowest_tScore
lowest_tScore = users[0].gettScore()
for element in users:
    if element.gettScore() < lowest_tScore:
        lowest_tScore = element.gettScore()
        person = element.getfName() + " " + element.getlName()

print(f"{person} has the lowest test score at: {lowest_tScore}!")
person = ""





