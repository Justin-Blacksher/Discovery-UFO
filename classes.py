# _________ [ Classes file ] ___________________
#  - Justin Blacksher
#  - 8/27/2022
#  - Classes file for Discovery UFO
# ______________________________________________


# __________ [ Authentication Class ] __________

class Authenticate:
    def __init__(self):
        self.name = "default"
        self.password = "default"
        self.verified = False
        self.loggedIn = False

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def setPassword(self, password):
        self.password = password
    def verifyName(self):
        pass
    def verifyPassword(self):
        pass
    def submitAuthentication(self):
        try:
            # Submit verified authentication
            pass
        except:
            print("Authentication Unsuccessful")
        finally:
            self.loggedIn = True
# ______________________________________________

# __________ [ Database Class ] ________________

# ______________________________________________