class MemberStore:
    members = []

    def get_all(self):
        #get all MemberStore
        return MemberStore.members

    last_id = 1
    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id = MemberStore.last_id + 1

    def get_by_id(self, id):
        #get member by id
        for m in MemberStore.members:
            if m.id == id:
                return m
        return None

    #def update(self, member):
        #update member data

    def delete(self, id):
        #delete member by id
        m = self.get_by_id(id)
        if m != None:
            MemberStore.members.remove(m)
            print "Member is deleted successfully..."
        else:
            print "This Member Is Already Not Found!!!"

    def entity_exists(self, member):
        #check if an entity exists in store
        if self.get_by_id(member.id) != None:
            return True
        else:
            return False

class PostStore:
    posts = []

    def get_all(self):
        #get all Posts
        return PostStore.posts

    def get_by_id(self, id):
        #get post by id
        for p in PostStore.posts:
            if p.id == id:
                return p
        return None

    last_id = 1
    def add(self, post):
        #add new post
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id = PostStore.last_id + 1

    #def update(self, post):
        #update post data

    def delete(self, id):
        #delete post by id
        p = self.get_by_id(id)
        if p != None:
            PostStore.posts.remove(p)
            print "Post is deleted successfully..."
        else:
            print "This Post Is Already Not Found!!!"

    def entity_exists(self, post):
        #check if an entity exists in store
        if self.get_by_id(post.id) != None:
            return True
        else:
            return False
