from models import Member, Post
from data_store import MemberStore, PostStore

member_store = MemberStore()
post_store = PostStore()

#Members functions==============================================================
def create_members():
    member1 = Member("Hassan", 35)
    member2 = Member("Kareem", 30)
    member3 = Member("Yousef", 25)
    return member1, member2, member3

def add_members_to_store(members_list):
    for m in members_list:
        member_store.add(m)

def update_member_data(member):
    new_member = Member(member.name, member.age)
    new_member.id = 1
    if new_member is not member:
        print "member and new_member are not the same object!!! "
    new_member.name = "Hanan"
    new_member.age = 40
    member_store.update(new_member)
    print "=" * 30

def delete_member(member_id):
    member_store.delete(member_id)
    print "=" * 30

def show_all_members():
    for m in member_store.members:
        print m
    print "=" * 30

def search_members_by_id(id):
    member = member_store.get_by_id(id)
    if member == None:
        print "No members found by this id!!!"
    return member
    print "=" * 30

def search_members_by_name(name):
    result_list = member_store.get_by_name(name)
    if len(result_list) == 0:
        print "No members found by this name!!!"
    else:
        for m in result_list:
            print m
    print "=" * 30

#Post functions=================================================================
def create_posts():
    post1 = Post("abc", "abcdefghijklm", member1.id )
    post2 = Post("def", "nopqrstuvwxyz", member1.id)
    post3 = Post("ghi", "0123456789", member2.id)
    return post1, post2, post3

def add_posts_to_store(posts_list):
    for p in posts_list:
        post_store.add(p)

def update_post(post):
    new_post = Post(post.address, post.message, 1)
    new_post.id = 2
    if new_post is not new_post:
        print "post and new_post are not the same object!!"
    new_post.address = "JKLMN"
    new_post.message = "Hello Everybody"
    post_store.update(new_post)
    print "=" * 30

def delete_post(post_id):
    post_store.delete(post_id)
    print "=" * 30

def show_all_posts():
    for p in post_store.posts:
        print p
    print "=" * 30

def search_posts_by_id(id):
    post = post_store.get_by_id(id)
    if post == None:
        print "No members found by this id!!!"
    return post
    print "=" * 30

#check all functions results====================================================
mList = create_members()
member1, member2, member3 = mList

add_members_to_store(mList)

show_all_members()

update_member_data(member1)

m = search_members_by_id(3)
if(m != None):
    print m.name
    print m.age

search_members_by_name("Kareem")

pList = create_posts()
post1, post2, post3 = pList

add_posts_to_store(pList)

show_all_posts()

update_post(post2)

p = search_posts_by_id(2)
if(p != None):
    print p.address
    print p.message
