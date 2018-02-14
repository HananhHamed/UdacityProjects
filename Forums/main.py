from models import Member, Post
from data_store import MemberStore, PostStore


member1 = Member("Hassan", 35)
member2 = Member("Kareem", 30)
member1.show_member_data()

post1 = Post()
post2 = Post()
post3 = Post()

member_store = MemberStore()
member_store.add(member1)
member_store.add(member2)

post_store = PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
