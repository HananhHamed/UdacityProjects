from models import Member, Post
from data_store import MemberStore, PostStore

member1 = Member("Hassan", 35)
member2 = Member("Kareem", 30)

post1 = Post("abc", "abcdefghijklm", member1.id )
post2 = Post("def", "nopqrstuvwxyz", member1.id)
post3 = Post("ghi", "0123456789", member2.id)

member_store = MemberStore()
member_store.add(member1)
member_store.add(member2)

post_store = PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
