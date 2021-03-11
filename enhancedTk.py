#                        Super_Tk GUI WINDOW OBJECT

#Created by JR016

#YOU MUST NEITHER TAKE COPYRIGHT FROM THIS SOFTWARE NOR COMMERCIALIZE IT
#THIS IS FREE OPEN-SOURCE SOFTWARE CREATED TO FACILITATE THE CREATION OF FRONT END PROJECTS


#THIS SCRIPT CONTAINS A MODIFIED VERSION OF THE tkinter.Tk() WINDOW OBJECT THAT I USED FOR THE "AFEPG"
#YOU CAN USE IT IN YOUR OWN GUI PROJECTS TOO IF YOU WANT TO.


#I PLUBLISHED THE PROGRAMME WITH THE SOURCE CODE SO YOU CAN CHECK IT AND CREATE YOUR OWN VERSION WITH
#NEW FEATURES AND STUFF
#ENJOY IT AND HAVE FUN
#:)

#IMPORTS

from tkinter import *
from PIL import ImageTk, Image #TO WORK WITH IMAGES
import sys, cGUIf #sys TO CLOSE THE GUI IF AN FATAL ERROR HAPPENS,

#cGUIf CLASS IS IMPORTED BECAUSE IT HAS FUNCTIONS FOR ERROR AND WARNING POP-UPS

class Super_Tk(Tk):
    """A version of tkinter Tk to programme GUI's faster."""

    def __init__(self, title = "", icon_path = "", width = 500,
                 height = 500, is_resizable = False):
        """Initialize GUI window with special attributes."""

        #Call Parent constructor method
        super(Super_Tk, self).__init__()

        #Set new title and icon_path if possible
        if isinstance(title,str):
            if len(title) > 0:
                self.title(title)

        else:
            cGUIf.show_error("TypeError", f'"title" must be of type str, not of type {type(title)}.')
            sys.exit(1)
            
        #Set window to not resizable
        if isinstance(is_resizable,bool):
            if not is_resizable:
                self.resizable(False,False)

        else:
            cGUIf.show_error("TypeError", f'"is_resizable" must be of bool type, not of type {type(is_resizable)}.')
            sys.exit(1)
        
        #Check if it is possible to apply an Image (Do some error handling)
        if isinstance(icon_path,str):
            if len(icon_path) > 0:
                try:
                    self.iconphoto(False, PhotoImage(file = icon_path))

                except TclError as tkerror:
                    cGUIf.show_error("Fatal Error", tkerror)
                    sys.exit(1) #Cancel all operations

        #Set window size if possible (Do some Error handling)

        if width != "" and height != "":
            try:
                self.geometry(f"{width}x{height}")

            except TclError as tkerror:
                cGUIf.show_error("Fatal Error", tkerror)
                sys.exit(1)


#Tell the user the program is not meant to be run directly
if __name__ == "__main__":

    cGUIf.show_warning("Import Warning", "This script containts a modified version " \
                       + "of Tk()\n(The Tkinter Window Object) for simple and fast GUI projects" \
                       + "\n\nThe script is NOT MEANT TO BE RUN DIRECTLY.\nPlease, IMPORT IT IN ANOTHER SCRIPT.")
