class User:
    def __init__(self, ids, name):
        self.id = ids
        self.name = name
        self.followers = 0
        self.following = 0


    def follow(self,user):
        user.followers += 1
        self.following += 1


user1 = User("022", "waluka")
user2 = User("021", "jay")
print(user1.following, user1.followers)
print(user2.following, user2.followers)
user1.follow(user2)
print(user1.following, user1.followers)
print(user2.following, user2.followers)