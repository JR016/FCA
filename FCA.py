#                                   App Script

#                  It runs the whole File Converter GUI App
#                   This App is avaliable for WINDOWS ONLY


#IMPORTS
from enhancedTk import Super_Tk
from Main_Frame import Main_Frame
import cGUIf, platform, os, sys


#GLOBAL CONSTANTS

WIDTH = 600
HEIGHT = 550
TITLE = "FCA"
ICON_FILENAME = os.path.join("pics","icon_2.png")

def main(): 
    """Runs the whole App."""

    #Check the OS is Windows
    is_windows = check_os()

    if is_windows:

        #Create a GUI window
        window = Super_Tk(TITLE,ICON_FILENAME,WIDTH,HEIGHT)

        #Initialize the Main Frame of the IAC App
        mainPage = Main_Frame(window,WIDTH,HEIGHT)
        mainPage.place(x = 0, y = 0)

        #Run GUI Mainloop (It always must be run at the end)
        window.mainloop()

    else:
        cGUIf.show_error("OS Incompatibility Error",
                         f"\n\nThe Operating System of this machine is {platform.system()}" \
                         + "\n\nThis app ONLY runs on Windows." \
                         + "\n\nThanks for trying, though.")


def check_os():
    """Confirms the OS of the computer is Windows."""

    selected_OS = "Windows"
    return platform.system() == selected_OS
    

if __name__ == "__main__": 
    main()
