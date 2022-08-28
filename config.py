#
#    Configuration.py
#    Window Configuration for DiscoverUFO
#    Justin Blacksher
#
from datetime import datetime

# _____________ [ Default Team Information ] ____________

myTeam = 'SLC001'
myArea = 'Antelope Island'

# ______________________________________________________

# _____________ [ Date information ] ___________________
date = datetime.now()
nowDate = date.date()

WINDOW_TITLE = "Discover UFO"
#ICON = "icon.ico"

HEIGHT = 600
WIDTH = 800

# ---- [ Colors ] --------------

HEADER = '#ABA9BF'
BACKGROUND = '#34113F'
BUTTON = '#ABA9BF'
TEXT = '#98CE00'
HEADER_TEXT = '#BEB7DF'

# ------------------------------

# ---- [ Fonts ] ---------------

FONT = './fonts/Silkscreen-Regular.tiff'

# ------------------------------

# ---- [ Label Texts ] ---------

TITLE_LABEL = 'UFO Discovery'
AREA_LABEL = f'Area Assigned: {myArea}'
TEAM_NAME = f'Team Name: {myTeam}'
CURRENT_DATE = f'Todays Date: {nowDate}' 

# -----------------------------

# _______ [ Login Window Texts ] ________

BUTTON_TEXT = "DUFO LOGIN"
USERNAME = "Username"
PASSWORD = "Password"
TEAMNAME = "Team"
LOGIN_TITLE = "Log in to Discovery UFO!"
LOGIN_HEIGHT = 200
LOGIN_WIDTH = 400
LOGIN_X = 100
LOGIN_Y = 100

# _______________________________________


