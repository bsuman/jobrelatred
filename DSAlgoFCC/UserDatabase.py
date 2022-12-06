# As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure
# to manage profile information (username, name and email) for 100 million users.
# It should allow the following operations to be performed efficiently:
#
# Insert the profile information for a new user.
# Find the profile information of a user, given their username
# Update the profile information of a user, given their username
# List all the users of the platform, sorted by username
# You can assume that usernames are unique.


# List some scenarios for testing the class methods insert, find, update and list_all.
#
# Insert:
# Inserting into an empty database of users
# Trying to insert a user with a username that already exists
# Inserting a user with a username that does not exist

# Find:
# finding user that exists
# finding user that does not exist in the list
# finding multiple users with the username
# finding user in an empty list

# Update:
# Updating the user, who is found in the list i.e. existing user information update
# Updating the user information who does not exist
# Updating the user information for multiple users with the username
# Updating the user information in an empty list
#
# Display:
# Display all the users in the database in a sorted fashion
# Display of empty list


# user class is used to store the user information like username, name and email
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    # function to get the official string representation of the object of user class, which can be used to construct the object of the class
    def __repr__(self):
        return "username = {},name = {} and email = {}".format(self.username, self.name, self.email)

    # function to get the string representation of the object of user class
    def __str__(self):
        return self.__repr__()


class UserDB:
    def __init__(self):
        self.database = []

    def insertuser(self, user):
        if len(self.database) == 0:
            self.database.append(user)
        else:
            for i in range(len(self.database)):
                if user.username > self.database[i].username:
                    self.database.insert(i, user)

    def finduser(self, user):
        if len(self.database) == 0:
            return "No user in DB"
        for i in range(len(self.database)):
            if user.username == self.database[i].username:
                return self.database[i]
        return "User not found !"

    def displayAllUsers(self):
        return self.database

    def updateUser(self,user):
        iuser = self.finduser(user.username)
        if iuser is type(User):
            iuser.name = user.name
            iuser.email = user.email
        else:
            print("User not found in database!")



class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users

if __name__ == '__main__':
    user_1 = User("bSuman","Suman","suman.darmstadt@gmail.com")
    user_2 = User("dontbSuman", "SumanNew", "sumannew.darmstadt@gmail.com")
    user_db = UserDatabase()
    user_db.insert(user_1)
    user_db.list_all()
    user_db.insert(user_2)

    print(user_db.find(user_1.username))
    print("=========================================================================")
    user_db_1= UserDB()
    user_db_1.insertuser(user_2)
    print(user_db_1.displayAllUsers())
    print(user_db_1.finduser(user_2))
    print(user_db_1.finduser(user_1))
    user_db_1.updateUser(User("dontbSuman", "Suman Bidarahalli", "suman.bidarahalli@gmail.com"))
    print(user_db_1.finduser(user_2))