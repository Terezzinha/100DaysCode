class User:

    def __int__(self, user_id, user_name):
        self.id - user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001","angela")
print(user_1.user_name)
