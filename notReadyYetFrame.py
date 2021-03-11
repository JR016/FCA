#                                  Not Ready Yet Frame Script

#                   This script represents the frame to be displayed when
#                a part of the frame is still in development and hasn't been
#                                         completed yet.


#IMPORTS
from tkinter import Frame
from tkinter import font
import Main_Frame #This one does not cause a "Circular Import Error"
import cGUIf, os

#GLOBAL CONSTANTS
FONTS = {
         "lucida grande" : "Lucida Grande",
         "cambria" : "Cambria",
         "times new roman" : "Times New Roman"
         }

ICON_FOLDER = "pics"

ICON_NAMES = ("neutral_face","bananinsin","back_arrow")

ICON_PATHS = (os.path.join(ICON_FOLDER,"icon_neutral_face.png"),
              os.path.join(ICON_FOLDER,"icon_JR016.png"),
              os.path.join(ICON_FOLDER,"icon_left_arrow.png"))


#Not Ready Yet Frame/Page class
class Not_Ready_Yet_Frame(Frame):
    """Frame to display when something is not ready yet.."""

    def __init__(self,master,width,height):
        """Initialize this frame with all the required information."""

        #Save inherited arguments
        self.master = master
        self.width = width
        self.height = height

        #Call parent's constructor method
        super(Not_Ready_Yet_Frame,self).__init__(master,
                                       width = width,
                                       height = height)

        #Dict of images
        self.__pics = self.pics_dict

        #Add the UI elements to the frame
        self.build_UI()

    @property
    def pics_dict(self):
        """Dictionary that contains the images of this frame."""

        #Add a for loop when the images of this frame are more than 3

        img_dict = {}
        
        neutral_pic = cGUIf.get_TkImage(ICON_PATHS[0],128,128)
        banana_pic = cGUIf.get_TkImage(ICON_PATHS[1],100,100)
        arrow_pic = cGUIf.get_TkImage(ICON_PATHS[2],32,32)
        
        img_dict.update({ICON_NAMES[0] : neutral_pic,
                         ICON_NAMES[1] : banana_pic,
                         ICON_NAMES[2] : arrow_pic})

        return img_dict

    def switch_frames(self):
        """Switch back to the Main Frame."""

        #Create new frame

        mainFrame = Main_Frame.Main_Frame(self.master,
                                          self.width,
                                          self.height)
        mainFrame.place(x = 0, y = 0)

        #Destroy this frame
        self.place_forget()
        self.destroy()
    

    def build_UI(self):
        """Contains the UI widgets of this frame."""

        #Common local coordinates to change the UI positions
        common_x = 0
        common_y = 0

        #Tell the user this frame is not ready to use yet

        #Create a big "Sorry" label
        self.sorryFont = font.Font(family = FONTS["lucida grande"], size = 35)
        self.sorryLabel = cGUIf.get_TextLabel(self,
                                              "Sorry",
                                              self.sorryFont,
                                              250 + common_x,
                                              30 + common_y)
        

        #Create a label to hold the indifferent face
        self.neutralFaceIcon = cGUIf.get_ImgLabel(self,
                                                  self.__pics["neutral_face"],
                                                  243 + common_x,
                                                  110 + common_y)

        #Create explanatory labels that says what's going on
        self.explanationFont = font.Font(family = FONTS["times new roman"], size = 15)
        self.explanationLabel1 = cGUIf.get_TextLabel(self,
                                                    "This part of the FCA has not been developed yet",
                                                    self.explanationFont,
                                                    120 + common_x,
                                                    270 + common_y)

        self.explanationLabel2 = cGUIf.get_TextLabel(self,
                                                     "JR016 is busy doing other things (Most of them irrevelant)",
                                                     self.explanationFont,
                                                     80 + common_x,
                                                     310 + common_y)

        self.explanationLabel3 = cGUIf.get_TextLabel(self,
                                                     "Please wait until this part of the FCA is ready",
                                                     self.explanationFont,
                                                     130 + common_x,
                                                     350 + common_y)

        self.explanationLabel4 = cGUIf.get_TextLabel(self,
                                                     "JR016 appreciates your patience",
                                                     self.explanationFont,
                                                     180 + common_x,
                                                     390 + common_y)

        #Add the JR016 Github icon
        self.bananinsinIcon = cGUIf.get_ImgLabel(self,
                                             self.__pics["bananinsin"],
                                                 255 + common_x,
                                                 420 + common_y)
        

        #Add a label that says "Back" for the back button
        self.backFont = font.Font(family = FONTS["cambria"],size = 12)
        self.backLabel = cGUIf.get_TextLabel(self,
                                             "Back",
                                             self.backFont,
                                             80 + common_x,
                                             489 + common_y)

        #Add a back button to go back to the main Frame
        self.backButton = cGUIf.get_Button(self,
                                           "",
                                           self.switch_frames,
                                           30 + common_x,
                                           480 + common_y)
        
        self.backButton.configure(image = self.__pics["back_arrow"])

        

        
        
        

            

def main(): 
    """Run warning if run directly"""

    warning_message = "This script contains the code that builds the " \
                      + "Doc page of the FCA (File Converter App)." \
                      + "\n\nThis script should NOT be run DIRECTLY." \
                      + "\n\nPlease, import it in another script."

    cGUIf.show_warning("Import warning",warning_message)




if __name__ == "__main__": 
    main()
