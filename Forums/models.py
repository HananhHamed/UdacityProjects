class  Member:
    def __init__(self, name , age ):
        self.name = name
        self.age = age
        self.member_list = []
        self.member_list.append(name)
        self.member_list.append(age)

    def show_member_data(self):
        print "Member name is "  + str(self.member_list[0])
        print "Member age is " + str(self.member_list[1])

class Post:
    def __init__(self):
        self.posts_list = []

    def add_new_post(self, address, message):
        new_post_list = []
        new_post_list.append(address)
        new_post_list.append(message)
        self.posts_list.append(new_post_list)

    def show_all_posts(self):
        if len(self.posts_list) > 0:
            for subject in self.posts_list:
                print subject[0]
                print subject[1]
        else:
            print "Sorry.You don't have any posts!!!"
