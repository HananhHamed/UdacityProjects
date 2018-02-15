from models import Member, Post
from data_store import MemberStore, PostStore


member1 = Member("Hassan", 35, 1)
member2 = Member("Kareem", 30, 2)

post1 = Post("abc", "abcdefghijklm", 1)
post2 = Post("def", "nopqrstuvwxyz", 2)
post3 = Post("ghi", "0123456789", 3)

member_store = MemberStore()
member_store.add(member1)
member_store.add(member2)


post_store = PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
