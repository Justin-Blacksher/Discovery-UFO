import config
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

# --------------------------------------------------

# ___________ [ Button Sets ] _____________

login = Button(root, command=functions.openLogin, font=FONT, text=config.BUTTON_TEXT)


# _________________________________________

# -------- [ Tk Label Widgits ] --------------------------

titleLabel = ttk.Label(root, text=config.TITLE_LABEL, background=config.BACKGROUND, foreground=config.TEXT, font=FONT, relief=RIDGE)
areaLabel = ttk.Label(root, text=config.AREA_LABEL, font=FONT, background=config.BACKGROUND, foreground=config.TEXT)
teamName = ttk.Label(root, text=config.TEAM_NAME, font=FONT,background=config.BACKGROUND, foreground=config.TEXT)
currDate = ttk.Label(root, text=config.CURRENT_DATE, font=FONT,background=config.BACKGROUND, foreground=config.TEXT)

# --------------------------------------------------

# ---------- [ TK Packs ] --------------------------

titleLabel.pack(fill=X)
areaLabel.pack(fill=X)
teamName.pack(fill=X)
currDate.pack(fill=X)
login.pack()

# --------------------------------------------------





root.mainloop()