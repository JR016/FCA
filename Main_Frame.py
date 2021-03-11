#                               Main Frame Script

#           This script represents the initial and main script of the IAC App
#            It contains the options the user can select for File Conversion


#IMPORTS
from tkinter import Frame
from tkinter import font
import notReadyYetFrame, ImageFrame, AudioFrame
import cGUIf, os


#GLOBAL CONSTANTS
FONTS = {"arial" : "Arial",
         "lucida grande" : "Lucida Grande",
         "courier" : "Courier",
         "courier new" : "Courier New",
         "cambria" : "Cambria",
         "georgia" : "Georgia",
         "times new roman" : "Times New Roman",
         "system" : "System"}

ICON_FOLDER = "pics"

ICON_NAMES = ("main_icon","image_icon","audio_icon","doc_icon","video_icon")

ICON_PATHS = (os.path.join(ICON_FOLDER,"icon_main.png"),
          os.path.join(ICON_FOLDER,"icon_image.png"),
          os.path.join(ICON_FOLDER,"icon_audio.png"),
          os.path.join(ICON_FOLDER,"icon_document.png"),
          os.path.join(ICON_FOLDER,"icon_video.png")
               )
    


#Main Frame/Page class
class Main_Frame(Frame):
    """Main frame of the Image/Audio Converter App."""
    

    def __init__(self,master,width,height):
        """Initialize this frame with all the required information."""

        #Save inherited arguments
        self.master = master
        self.width = width
        self.height = height

        #Call parent's constructor method
        super(Main_Frame,self).__init__(master,
                                        width = width,
                                        height = height)

        #List of images
        self.__pics = self.pics_dict

        #Tuple of acceptable frame names
        self.__frame_names = ("image_frame",
                              "audio_frame",
                              "doc_frame",
                              "video_frame")

        #Add the UI elements to the frame
        self.build_UI()
        

    @property
    def pics_dict(self):
        """Dictionary that contains the images of this frame."""

        img_dict = {}

        for name, path in zip(ICON_NAMES,ICON_PATHS):

            if name == "main_icon":
                tk_pic = cGUIf.get_TkImage(path,32,32)

            else:
                tk_pic = cGUIf.get_TkImage(path,64,64)
                
            img_dict.update({name : tk_pic})

        return img_dict
    

    def switch_frames(self, new_frameName):
        """Switch to another frame of the app."""

        if new_frameName in self.__frame_names:

            #Give rise to a new frame

            if new_frameName == "image_frame":
                image_frame= ImageFrame.Image_Frame(self.master,
                                                    self.width,
                                                    self.height)
                image_frame.place(x = 0, y = 0)
               

            elif new_frameName == "audio_frame":
                audio_frame = AudioFrame.Audio_Frame(self.master,
                                                     self.width,
                                                     self.height)
                audio_frame.place(x = 0, y = 0)

            elif new_frameName == "doc_frame":
                not_yet = notReadyYetFrame.Not_Ready_Yet_Frame(self.master,
                                                               self.width,
                                                               self.height)
                not_yet.place(x = 0, y = 0)

            else:
                not_yet = notReadyYetFrame.Not_Ready_Yet_Frame(self.master,
                                                               self.width,
                                                               self.height)
                not_yet.place(x = 0, y = 0)

            #Destroy the current frame
            self.place_forget()
            self.destroy()

    def build_UI(self):
        """Contains the UI widgets of this frame."""

        #Common local coordinates to change the UI positions
        common_x = 0
        common_y = 5

        #Create the Main Title
        self.titleFont = font.Font(family = FONTS["lucida grande"], size = 30)
        self.title = cGUIf.get_TextLabel(self,
                                         "File  Converter  App ",
                                         self.titleFont,
                                         135 + common_x,
                                         40 + common_y)

        #Add the "Main Icon"
        self.mainIcon = cGUIf.get_ImgLabel(self,
                                           self.__pics["main_icon"],
                                           280 + common_x,
                                           125 + common_y)


        #Create a subtitle that says "options"
        self.subtitleFont = font.Font(family = FONTS["courier new"], size = 22)
        self.subtitle = cGUIf.get_TextLabel(self,
                                           "Options",
                                            self.subtitleFont,
                                            240 + common_x,
                                            195 + common_y)

        #Create a label that says "Image Conversion"
        self.conversionFont = font.Font(family = FONTS["times new roman"], size = 15)
        self.imageConversionLabel = cGUIf.get_TextLabel(self,
                                              "      Image\n Conversion",
                                              self.conversionFont,
                                              60 + common_x,
                                              285 + common_y)

        #Create a button for Image Conversion
        self.imageButton = cGUIf.get_Button(self,
                                      "",
                                      lambda : self.switch_frames("image_frame"),
                                      190 + common_x,
                                      270 + common_y)
        self.imageButton.configure(image = self.__pics["image_icon"])

        #Create a label that says "Audio Conversion"
        self.audioConversionLabel = cGUIf.get_TextLabel(self,
                                                   "     Audio\n Conversion",
                                                   self.conversionFont,
                                                   440 + common_x,
                                                   285 + common_y)

        #Create a button for Audio Conversion
        self.audioButton = cGUIf.get_Button(self,
                                            "",
                                            lambda : self.switch_frames("audio_frame"),
                                            340 + common_x,
                                            270 + common_y)
        self.audioButton.configure(image = self.__pics["audio_icon"])

        #Create a label that says "Doc Conversion"
        self.docConversionLabel = cGUIf.get_TextLabel(self,
                                                      "       Doc\n Conversion",
                                                      self.conversionFont,
                                                      60 + common_x,
                                                      410 + common_y)


        #Create a button for Doc Conversion
        self.docButton = cGUIf.get_Button(self,
                                          "",
                                          lambda : self.switch_frames("doc_frame"),
                                          190 + common_x,
                                          400 + common_y)
        self.docButton.configure(image = self.__pics["doc_icon"])


        #Create a label that says "Video Conversion"
        self.videoConversionLabel = cGUIf.get_TextLabel(self,
                                                        "     Video\n Conversion",
                                                        self.conversionFont,
                                                        440 + common_x,
                                                        410 + common_y)

        #Create a button for Video Conversion
        self.videoButton = cGUIf.get_Button(self,
                                            "",
                                            lambda : self.switch_frames("video_frame"),
                                            340 + common_x,
                                            400 + common_y)
        self.videoButton.configure(image = self.__pics["video_icon"])
        
        



def main(): 
    """Run warning if run directly."""

    warning_message = "This script contains the code that builds the " \
                      + "main page of the FCA (File Converter App)." \
                      + "\n\nThis script should NOT be run DIRECTLY." \
                      + "\n\nPlease, import it in another script."

    cGUIf.show_warning("Import warning",warning_message)




if __name__ == "__main__": 
    main()
