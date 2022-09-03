# _________ [ Classes file ] ___________________
#  - Justin Blacksher
#  - 8/27/2022
#  - Classes file for Discovery UFO
# ______________________________________________

import config
import uuid
from tkinter import Entry, Label, Toplevel
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

# __________ [ Investigation File Classes ] ______

class lattitude:
    def __init__(self):
        self.degrees = 0
        self.minutes = 0
        self.seconds = 0
        self.direction = None
        self.latDec = None

    def getDegrees(self):
        pass
        
    def setDegrees(self, degrees):
        pass

    def getMinutes(self):
        pass

    def setMinutes(self, minutes):
        pass
    
    def getSeconds(self):
        pass

    def setSeconds(self):
        pass

    def getDirection(self):
        pass

    def setDirection(self):
        pass

    def getLatDec(self):
        pass

    def setLatDec(self):
        pass

    def calcDec(self):
        self.latDec = self.degrees + ((self.minutes/60) + (self.seconds/3600))
        
    def calcDeg(self, lat):
        # degrees = first whole number
        # minutes = whole number of remaining dec * 60
        # seconds = whole number of remaining dec * 60
        # _____________ [ EXAMPLE ] ______________
        # 40.657
        # deg = 40, min = .657 * 60, sec = (.657 * 60) * 60
        pass

class longitude:
    def __init__(self):
        self.degrees = 0
        self.minutes = 0
        self.seconds = 0
        self.direction = None
        self.longDec = None

    def getDegrees(self):
        pass
        
    def setDegrees(self, degrees):
        pass

    def getMinutes(self):
        pass

    def setMinutes(self, minutes):
        pass
    
    def getSeconds(self):
        pass

    def setSeconds(self):
        pass

    def getDirection(self):
        pass

    def setDirection(self):
        pass

    def getLatDec(self):
        pass

    def setLatDec(self):
        pass

    def calcDec(self):
        pass

    def calcDeg(self):
        pass

class InvestigationSightingIDGenerater:
    def __init__(self):
        self.localID = None
        self.globalID = None

    def setLocalID(self):
        self.localID = uuid.uuid4()
    def setGlobalID(self):
        self.globalID = uuid.uuid4()
    def getLocalID(self):
        return self.localID
    def getGlobalID(self):
        return self.globalID
    

class InvestigationLocation:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.sightingLocalID = None
        self.sightingGlobalID = None
        self.lattitude = None
        self.longitude = None

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getLastName(self):
        return self.lastName

    def setSightingLocalID(self):
        getID = InvestigationSightingIDGenerater()
        getID.setLocalID()
        L_ID = getID.getLocalID()
        self.sightingLocalID = L_ID

    def setSightingGlobalID(self):
        getGID = InvestigationSightingIDGenerater()
        getGID.setGlobalID()
        G_ID = getGID.getGlobalID()
        self.sightingGlobalID = G_ID


    def setLattitude(self):
        pass

    def setLongitude(self):
        pass

    def getSightingLocalID(self):
        return self.sightingLocalID

    def getSightingGlobalID(self):
        return self.sightingGlobalID

class InvestigationFile:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.l_ID = None
        self.g_ID = None
        self.locations = {} # dict of InvestigationLocation objects

    def addLocation(self, location): # Accepts an investigation location object 
        loc = InvestigationLocation()
        glo = InvestigationLocation()
        loc.setSightingLocalID()
        self.l_ID = loc.getSightingLocalID()
        glo.setSightingGlobalID()
        self.g_ID = glo.getSightingGlobalID()
        localString = f'{loc.sightingLocalID}_{loc.lastName}'
        globalString = f'{glo.sightingGlobalID}_{loc.lastName}'
        
        self.locations[localString] = {"First_Name": loc.firstName,
                                       "Last_Name": loc.lastName,
                                       "Lattitude": loc.lattitude,
                                       "Longitude": loc.longitude,
                                       "LocalID": loc.getSightingLocalID,
                                       "GlobalID": glo.getSightingGlobalID}
        self.locations[globalString] = {"First_Name": loc.firstName,
                                       "Last_Name": loc.lastName,
                                       "Lattitude": loc.lattitude,
                                       "Longitude": loc.longitude,
                                       "LocalID": loc.getSightingLocalID,
                                       "GlobalID": glo.getSightingGlobalID}
    
    def openInvestigationWindow(self):
        windowInvestigation = Toplevel()
        windowInvestigation.title = config.INVWINDOW
        windowInvestigation.geometry(f'{config.INVHEIGHT}x{config.INVWIDTH}+{config.INVX}+{config.INVY}')
        windowInvestigation.configure(background=config.BACKGROUND)
        windowInvestigation.resizable(False,False)
        labels = ['First Name', 'Last Name', 'Lattitude', 'Longitude']
        for lab in labels:
            Label(windowInvestigation, text=lab, font=config.FONT, background=config.BACKGROUND, foreground=config.TEXT).pack()
            Entry(windowInvestigation, show=None).pack()
        Label(windowInvestigation, text="____ [ Global ID ] ____", font=config.FONT, background=config.BACKGROUND, foreground=config.TEXT).pack()
        Label(windowInvestigation, text=self.g_ID, font=config.FONT, background=config.BACKGROUND, foreground=config.HEADER_TEXT).pack()
        Label(windowInvestigation, text="____ [ Local ID ] ____", font=config.FONT, background=config.BACKGROUND, foreground=config.TEXT).pack()
        Label(windowInvestigation, text=self.l_ID, font=config.FONT, background=config.BACKGROUND, foreground=config.HEADER_TEXT).pack()
# ______________________________________________