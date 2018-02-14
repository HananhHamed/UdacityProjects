class MemberStore:
    members = []

    def get_all(self):
        #get all MemberStore
        return members

    def get_by_id(self, id):
        #get member by id

    def add(self, member):
        #append member
        MemberStore.members.append(member)

    def update(self, member):
        #update member data

    def delete(self, id):
        #delete member by id

    def entity_exists(self, member):
        #check if an entity exists in store

class PostStore:
    posts = []

    def get_all(self):
        #get all Posts
        return Posts

    def get_by_id(self, id):
        #get post by id

    def add(self, post):
        #add new post
        Posts.append(post)

    def update(self, post):
        #update post data

    def delete(self, id):
        #delete post by id
