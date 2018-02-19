class MemberStore():
    members = []
    last_id = 1

    def get_all(self):
        #get all MemberStore
        return MemberStore.members

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id = MemberStore.last_id + 1

    def get_by_id(self, id):
        #get member by id
        member_lst = self.get_all()
        for m in member_lst:
            if m.id == id:
                return m
        return None

    def get_by_name(self, name):
        #get member by name
        search_result_list = []
        member_lst = self.get_all()
        for m in member_lst:
            if m.name == name:
                search_result_list.append(m)
        return search_result_list

    def update(self, member):
        #update member data
        member_id = member.id
        member_lst = self.get_all()
        for m in member_lst:
            if m.id == member_id:
                m = member
                print "Data Updated Succesfully..."

    def delete(self, id):
        #delete member by id
        m = self.get_by_id(id)
        if m is not None:
            MemberStore.members.remove(m)
            print "Member is deleted successfully..."
        else:
            print "This Member Is Already Not Found!!!"

    def entity_exists(self, member):
        #check if an entity exists in store
        if self.get_by_id(member.id) is not None:
            return True
        else:
            return False

class PostStore():
    posts = []
    last_id = 1

    def get_all(self):
        #get all Posts
        return PostStore.posts

    def get_by_id(self, id):
        #get post by id
        post_lst = self.get_all()
        for p in post_lst:
            if p.id == id:
                return p
        return None

    def add(self, post):
        #add new post
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id = PostStore.last_id + 1

    def update(self, post):
        #update post data
        post_id = post.id
        post_lst = self.get_all()
        for p in post_lst:
            if p.id == post_id:
                 p.address = post.address
                 p.message = post.message
                 print "Post Edited successfully..."

    def delete(self, id):
        #delete post by id
        p = self.get_by_id(id)
        if p is not None:
            PostStore.posts.remove(p)
            print "Post is deleted successfully..."
        else:
            print "This Post Is Already Not Found!!!"

    def entity_exists(self, post):
        #check if an entity exists in store
        if self.get_by_id(post.id) is not None:
            return True
        else:
            return False
