class  Member:
    def __init__(self, name , age ):
        self.name = name
        self.age = age
        self.id = 0


class Post:
    def __init__(self, address, message, member_id):
        self.address = address
        self.message = message
        self.id = 0
        self.member_id = member_id
