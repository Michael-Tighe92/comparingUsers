data = []
dataItem = []
users = []

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
    def getFullName(self):
        return f"User's full name is: {self.fName} {self.lName}"
    
    def getAge(self):
        return f"{self.fName} is {self.age} years old"
    
    def getpNum(self):
        return f"{self.fName}'s phone number is: {self.pNum}"

    def getEmail(self):
        return f"{self.fName}'s email is: {self.email}"

    def gettScore(self):
        return self.tScore

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
    users.append(User(dataItem[0],dataItem[1],dataItem[2],dataItem[3],dataItem[4],dataItem[5]))
    dataItem.clear()

myFile.close()

# recieves all user's names
for element in users:
    print(element.getFullName())

# comparing test scores



