import itertools
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
        member_lst = self.get_all()
        return (m for m in member_lst if m.name == name)

    def update(self, member):
        #update member data
        member_id = member.id
        member_lst = self.get_all()
        for i, m in enumerate(member_lst):
            if m.id == member_id:
                member_lst[i] = member
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

    def get_members_with_posts(self, all_posts):
        #get all members but each member with all his posts
        all_members = self.get_all()
        for m, p in itertools.product(all_members, all_posts):
            if m.id == p.member_id :
                m.posts.append(p)
        for m in all_members:
            yield m

        #================================================================================
    def get_top_ten(self, all_posts):
        members_with_post_list = self.get_members_with_posts(all_posts)
        sorted_lst = sorted(members_with_post_list, key=lambda p: len(p.posts), reverse=True)
        return sorted_lst[:2]

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
        for i, p in enumerate(post_lst):
            if p.id == post_id:
                 post_lst[i] = post
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
