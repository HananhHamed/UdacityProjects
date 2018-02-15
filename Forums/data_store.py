class MemberStore:
    members = []

    def get_all(self):
        #get all MemberStore
        return MemberStore.members


    def add(self, member):
        MemberStore.members.append(member)

    #def get_by_id(self, id):
        #get member by id

    #def update(self, member):
        #update member data

    #def delete(self, id):
        #delete member by id

    #def entity_exists(self, member):
        #check if an entity exists in store

class PostStore:
    posts = []
    def get_all(self):
        #get all Posts
        return PostStore.posts

    #def get_by_id(self, id):
        #get post by id

    def add(self, post):
        #add new post
        PostStore.posts.append(post)

    #def update(self, post):
        #update post data

    #def delete(self, id):
        #delete post by id
