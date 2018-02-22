class  Member():
    def __init__(self, name , age ):
        self.name = name
        self.age = age
        self.id = 0
        self.posts = []

    def __str__(self):
        return "Name: "+ self.name +" Age: " + str(self.age)

#==============================================================

class Post():
    def __init__(self, address, message, member_id = 0):
        self.address = address
        self.message = message
        self.id = 0
        self.member_id = member_id

    def __str__(self):
        return "Title: " + self.address + " Content: " + self.message
