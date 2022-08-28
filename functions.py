# _______________________ [ Functions relating to buttons ] _________________________
# - Justin Blacksher
# - 8/27/2022
# - Discovery UFO
# ___________________________________________________________________________________


from tkinter import Entry, Label, Toplevel
from classes import Authenticate
import config

# _______________________ [ Lambda ] ______________________________



# _________________________________________________________________


# _______________________ [ LOGIN PAGE ] __________________________

def openLogin():
    def getUser():
        return userEntry.get()

    def getPass():
        return passEntry.get() 


    loginWindow = Toplevel()
    loginWindow.title = config.LOGIN_TITLE
    loginWindow.geometry(f"{config.LOGIN_HEIGHT}x{config.LOGIN_WIDTH}+{config.LOGIN_X}+{config.LOGIN_Y}")
    loginWindow.configure(background=config.BACKGROUND)
    Label(loginWindow, text=config.USERNAME, font=config.FONT, background=config.BACKGROUND, foreground=config.TEXT).pack()
    userEntry = Entry(loginWindow, show=None).pack()
    Label(loginWindow, text=config.PASSWORD, font=config.FONT, background=config.BACKGROUND, foreground=config.TEXT).pack()
    passEntry = Entry(loginWindow, show='*').pack()

    



def submitCredentials(userName, password):
    auth = Authenticate()
    auth.setName(userName)
    auth.setPassword(password)
    auth.verifyName()
    auth.verifyPassword()
    auth.submitAuthentication()



#__________________________________________________________________


# _______________________ [ MAIN PAGE ] ___________________________

def submitSighting():
    # Submit password and username for verification
    pass

def lookupSighting():
    # Create query for database
    pass



# _________________________________________________________________


# _______________________ [ SUBSEQUENT PAGES ] ____________________

# _________________________________________________________________
