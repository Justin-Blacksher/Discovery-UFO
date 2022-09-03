import config
import classes
from PIL import ImageTk
from tkinter import *
from tkinter import ttk
from tkextrafont import Font
import functions
root = Tk()

FONT = Font(file="C:/Users/Black/OneDrive/Documents/UFOdiscovery/fonts/Silkscreen-Regular.ttf", family="Silkscreen")

# ---------- [ Bring in the configuration ] --------

window_height = config.HEIGHT
window_width = config.WIDTH
window_title = config.WINDOW_TITLE
#window_icon = config.ICON
c_image = config.ALIEN

# --------------------------------------------------

# ---------- [ Find the center point ] -------------

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# --------------------------------------------------

# ---------- [ Configure the Window ] --------------

root.title(window_title)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.configure(bg=config.HEADER)
#root.iconbitmap(window_icon)
canvas = Canvas(root, width=window_width, height=window_height)


# --------------------------------------------------

# ___________ [ Button Sets ] _____________

login = Button(root, command=functions.openLogin, font=FONT, text=config.BUTTON_TEXT, bg=config.BACKGROUND, fg=config.BUTTON)
currentInvestigation = classes.InvestigationFile()
currentInvestigation.addLocation(40.345)
newInvestigation = Button(root, command=currentInvestigation.openInvestigationWindow, font=FONT, text=config.START_INV, bg=config.BACKGROUND, fg=config.BUTTON)

# _________________________________________

# -------- [ Tk Label Widgits ] --------------------------

titleLabel = ttk.Label(root, text=config.TITLE_LABEL, background=config.BACKGROUND, foreground=config.TEXT, font=FONT, relief=RIDGE)
areaLabel = ttk.Label(root, text=config.AREA_LABEL, font=FONT, background=config.BACKGROUND, foreground=config.TEXT)
teamName = ttk.Label(root, text=config.TEAM_NAME, font=FONT,background=config.BACKGROUND, foreground=config.TEXT)
currDate = ttk.Label(root, text=config.CURRENT_DATE, font=FONT,background=config.BACKGROUND, foreground=config.TEXT)



# --------------------------------------------------

# ---------- [ TK Packs ] --------------------------
newInvestigation.pack(fill=X)
login.pack(fill=X)
titleLabel.pack(fill=X)
areaLabel.pack(fill=X)
teamName.pack(fill=X)
currDate.pack(fill=X)
canvas.pack()




# --------------------------------------------------
img = ImageTk.PhotoImage(file=c_image)
canvas.create_image(350,350,image=img)




root.mainloop()