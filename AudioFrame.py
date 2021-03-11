#                                    Audio Frame Script
#                       This script builds the UI of the FCA Audio Frame
#                                     and its behaviour


#IMPORTS
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from pydub import AudioSegment
import Main_Frame, os, cGUIf


#GLOBAL CONSTANTS
FONTS = {"lucida grande" : "Lucida Grande",
         "courier" : "Courier",
         "cambria" : "Cambria",
         "helvetica" : "Helvetica",
         "georgia" : "Georgia",
         "system" : "System"}

ICON_FOLDER = "pics"

ICON_NAMES = ("audio_icon","back_arrow")

ICON_PATHS = (os.path.join(ICON_FOLDER,"icon_audio.png"),
              os.path.join(ICON_FOLDER,"icon_left_arrow.png"))

FORMATS = ("MP3", "WAV", "OGG")


EXTS_N_NAMES = {".mp3" : "MP3",
                ".wav" : "WAV",
                ".ogg" : "OGG"}

NAMES_N_EXTS = {"MP3" : ".mp3",
                "WAV": ".wav",
                "OGG" : ".ogg"}


#Audio Frame/Page class
class Audio_Frame(Frame):
    """Frame for the Audio File Conversion."""

    def __init__(self,master,width,height):
        """Initialize this frame with all the required information."""

        #Save inherited arguments
        self.master = master
        self.width = width
        self.height = height

        #Call parent's constructor method
        super(Audio_Frame,self).__init__(master,
                                         width = width,
                                         height = height)

        #Dict of images
        self.__pics = self.pics_dict

        #Attributes to handle GUI operations
        self.times_file_asked = 0 #Times user asked for an input file audio
        self.times_folder_asked = 0 #Times the user asked for an output location

        self.__no_errors = True #Boolean variable that holds True when there is no errors

        #Add the UI elements to the frame
        self.build_UI()


    @property
    def pics_dict(self):
        """Dictionary that contains the images of this frame."""

        img_dict = {}

        for name, path in zip(ICON_NAMES, ICON_PATHS):

            tk_pic = cGUIf.get_TkImage(path,32,32)
            img_dict.update({name : tk_pic})

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


    def ask_audioFile(self):
        """Allows the user to browse his/her computer for an audio file"""

        #Tuple of the other input entry widgets
        otherInputEntryWidgets = (self.fileNameEntry,
                                  self.fileLocationEntry,
                                  self.fileFormatEntry)

        #Let the user select an audio file from its file system
        self.input_audioFile = filedialog.askopenfilename(title = "Select an Audio File",
                                                          filetypes = (
                                                              ("Audio Files", "*.mp3 *.wav *.ogg"),
                                                              ("MP3 Files", "*.mp3"),
                                                              ("WAV Files", ".wav"),
                                                              ("OGG Files", "*.ogg"))
                                                          )

        self.inputFileEntry.configure(state = "default")

        #If the file is unnamed "It onlt has the file extension", do not consider it
        if len(os.path.basename(self.input_audioFile)) < 5 and len(self.input_audioFile) != 0:
            cGUIf.show_error("Unnamed Audio File Error",
                             "This programme does not deal with unnamed audio files.")

            self.inputFileEntry.delete(0, END)

            #Also clear the other input entry widgets
            for otherEntry in otherInputEntryWidgets:

                if len(otherEntry.get()) > 0:
                    otherEntry.configure(state = "default")
                    otherEntry.delete(0, END)
                    otherEntry.configure(state = "readonly")
                    

        elif len(self.input_audioFile) != 0:

            #Increase the times the user pressed the button
            self.times_file_asked += 1

            #Delete previous content if it exists
            if self.times_file_asked > 1:

                self.inputFileEntry.delete(0, END)

            #Add audio file path to entry widget when selected
            self.inputFileEntry.insert(0, self.input_audioFile)
            self.inputFileEntry.configure(state = "readonly")

            #Show the info in the input fields
            self.show_fileInfo()

        else:
            pass


    def show_fileInfo(self):
        """Shows the info of the input file in the corresponding entry widgets."""

        #Get the info about the file
        self.file_name = os.path.basename(self.input_audioFile)[:-4]
        self.file_location = os.path.dirname(os.path.abspath(self.input_audioFile))
        self.file_format = EXTS_N_NAMES[os.path.splitext(self.input_audioFile)[1]]

        #Get a tuple of the entry widgets
        input_entryWidgets = (self.fileNameEntry,
                              self.fileLocationEntry,
                              self.fileFormatEntry)

        #Get a tuple of the input info
        input_info = (self.file_name,
                      self.file_location,
                      self.file_format)

        #Use a for loop to handle the info
        for entry_widget, info in zip(input_entryWidgets, input_info):

            #Make the widget go to default state
            entry_widget.configure(state = "default")

            #Clear the widgets of any previous content
            if self.times_file_asked > 1:
                entry_widget.delete(0, END)

            #Add content
            entry_widget.insert(0, info)

            #Make the widget go readonly again
            entry_widget.configure(state = "readonly")


    def ask_folder(self):
        """Allows the user to browse his/her PC for a folder location."""

        #Let the user select a folder
        self.output_folder = filedialog.askdirectory()

        #Increase the times the user pressed the button
        self.times_folder_asked += 1

        self.outputFileLocationEntry.configure(state = "default")

        #Delete previous content in the entry widget if any exists
        if self.times_folder_asked > 1:
            self.outputFileLocationEntry.delete(0, END)

        #Add the output folder path to the entry widget when selected
        self.outputFileLocationEntry.insert(0, self.output_folder)
        self.outputFileLocationEntry.configure(state = "readonly")

    def check_conversion(self):
        """Makes sure there is no errors for the conversion"""

        #Check that all is alright

        #Make a tuple of all input entry widgets
        all_inputEntryWidgets = (self.inputFileEntry,
                                 self.fileNameEntry,
                                 self.fileLocationEntry,
                                 self.fileFormatEntry)

        #Check that the user entered an input image file before clicking the conversion button
        if len(self.inputFileEntry.get()) == 0:
            cGUIf.show_warning("Upload Audio File Warning",
                               "You have to upload an audio file first" \
                               + " to convert it to another format")

            self.__no_errors = False

        #Check that the input file entered by the user exists by conversion time
        if not os.path.exists(self.inputFileEntry.get()) and len(self.inputFileEntry.get()) > 0:
            cGUIf.show_error("File Not Found Error",
                             f"The file {self.inputFileEntry.get()} was not found " \
                             + "in your file system.\n\nIt might have been deleted" \
                             + " or moved to another location.")

            #Clear all input related entry widgets
            for entry_widget in all_inputEntryWidgets:
                entry_widget.configure(state = "default")
                entry_widget.delete(0, END)
                entry_widget.configure(state = "readonly")


            self.__no_errors = False

        #If a location is entered for the output folder, check that it exists
        # at the time the user clicked the conversion button
        if not os.path.exists(self.outputFileLocationEntry.get()) and len(self.outputFileLocationEntry.get()) > 0:
            cGUIf.show_error("Folder Not Found Error",
                             f"The folder {self.outputFileLocationEntry.get()} was not found in your file system" \
                             + "\n\nIt might have been deleted or moved to another location.")

            #Clear the entry output widget
            self.outputFileLocationEntry.configure(state = "default")
            self.outputFileLocationEntry.delete(0, END)
            self.outputFileLocationEntry.configure(state = "readonly")

            self.__no_errors = False


        #Check that the file formats of the input and the output file are different
        if self.fileFormatEntry.get() == self.chosenFormat.get():
            cGUIf.show_error("Same Format Error",
                             f"Can't convert a {self.file_format} file to a {self.chosenFormat.get()} file" \
                             + " because their file format is the same.")

            self.__no_errors = False
            
        

    def convert_command(self):
        """Executes all conversion operations."""

        self.__no_errors = True #Assume there is no errors when the button is clicked

        self.check_conversion()

        if self.__no_errors:
            #This code will contain the convertion operations
            self.handle_conversion()
            

    def handle_conversion(self):
        """Convert one type of audio file to another one."""

        #Build the file path of the output image file

        #If user hasn't specified a location for the output audio file
        #It will be the location of the input audio file

        if len(self.outputFileLocationEntry.get()) == 0:
            output_fileLocation = self.file_location

        else:
            output_fileLocation = self.outputFileLocationEntry.get()

        #The output file audio will have the same name as the input audio file
        output_fileName = self.file_name

        #The format will be specified by the user
        output_fileFormat = NAMES_N_EXTS[self.chosenFormat.get()]

        #Assemble the output audio file
        output_fileNameWithExt = output_fileName + output_fileFormat

        output_completeFileName = os.path.join(output_fileLocation,
                                               output_fileNameWithExt)

        #Do the conversion
        audio_file = AudioSegment.from_file(self.inputFileEntry.get())
        audio_file.export(output_completeFileName)
        

        cGUIf.show_info("Successful Conversion Pop Up",
                        f"You sucessfully converted a {self.file_format} audio file" \
                        + f" to a {self.chosenFormat.get()} audio file.")


    def build_UI(self):
        """Contains the UI widgets of this frame."""

        #Common local coordinates to change UI positions
        common_x = 0
        common_y = -15


        #Create a big label that says "Audio File Conversion"
        self.titleFont = font.Font(family = FONTS["lucida grande"], size = 30)
        self.titeLabel = cGUIf.get_TextLabel(self,
                                             "Audio File Conversion",
                                             self.titleFont,
                                             120 + common_x,
                                             40 + common_y)
        

        #Create an image label for the audio icon
        self.audioIcon = cGUIf.get_ImgLabel(self,
                                            self.__pics["audio_icon"],
                                            295 + common_x,
                                            115 + common_y)


        #Create a label for the entry widget
        self.entryLabelFont = font.Font(family = FONTS["courier"], size = 13)
        self.entryLabel = cGUIf.get_TextLabel(self,
                                              "File to upload:",
                                              self.entryLabelFont,
                                              55 + common_x,
                                              180 + common_y)
        

        #Create an entry widget for the Input File
        self.entryFont = font.Font(family = FONTS["cambria"], size = 12)
        self.inputFileEntry = cGUIf.get_Entry(self,
                                              self.entryFont,
                                              225 + common_x,
                                              180 + common_y)

        self.inputFileEntry.configure(state = "readonly")


        #Create a button that allows the user to browse his/her file system
        self.inputFileButton = cGUIf.get_Button(self,
                                                "Browse",
                                                self.ask_audioFile,
                                                450 + common_x,
                                                180 + common_y)

        #Create a label that says "Input File Info"
        self.labelFont = font.Font(family = FONTS["georgia"], size = 17)
        self.inputFileInfo = cGUIf.get_TextLabel(self,
                                                 "Input File\n     Info",
                                                 self.labelFont,
                                                 120 + common_x,
                                                 240 + common_y)
        

        #Create a label that says "File Name"
        self.timeNameEntryLabel = cGUIf.get_TextLabel(self,
                                                      "File Name:",
                                                      self.entryLabelFont,
                                                      30 + common_x,
                                                      320 + common_y)

        #Create a readonly entry widget for the input file name
        self.fileNameEntry = cGUIf.get_Entry(self,
                                             self.entryFont,
                                             190 + common_x,
                                             320 + common_y)

        #Configure the entry widget so it is readonly and its width is shorter
        self.fileNameEntry.configure(state = "readonly", width = 12)
        

        #Create a label that says "File Location."
        self.fileLocationEntryLabel = cGUIf.get_TextLabel(self,
                                                          "File Location:",
                                                          self.entryLabelFont,
                                                          30 + common_x,
                                                          360 + common_y)

        #Create a readonlt entry widget for the input file location
        self.fileLocationEntry = cGUIf.get_Entry(self,
                                                 self.entryFont,
                                                 190 + common_x,
                                                 360 + common_y)

        #Configure the entry widget to be readonly and shorter
        self.fileLocationEntry.configure(state = "readonly", width = 12)


        #Create a label that says "File Format"
        self.fileFormatEntryLabel = cGUIf.get_TextLabel(self,
                                                        "File Format:",
                                                        self.entryLabelFont,
                                                        30 + common_x,
                                                        400 + common_y)


        #Create a readonly entry widget for the file format
        self.fileFormatEntry = cGUIf.get_Entry(self,
                                               self.entryFont,
                                               190 + common_x,
                                               400 + common_y)
        

        #Configure the entry widget to be readonly and shorter
        self.fileFormatEntry.configure(state = "readonly", width = 12)


        #Create a label that says "Conversion Options"
        self.conversionOptionsLabel = cGUIf.get_TextLabel(self,
                                                          "Conversion\n   Options",
                                                          self.labelFont,
                                                          400 + common_x,
                                                          240 + common_y)

        #Create a StringVar object that holds the option
        self.chosenFormat = StringVar()
        self.chosenFormat.set("MP3")


        #Create a label for the MP3 Radiobutton
        self.radioButtonFont = font.Font(family = FONTS["system"], size = 15)

        self.mp3RadioLabel = cGUIf.get_TextLabel(self,
                                                 FORMATS[0],
                                                 self.radioButtonFont,
                                                 455 + common_x,
                                                 320 + common_y)

        #Create a Radiobutton for MP3
        self.mp3Radiobutton = cGUIf.get_Radiobutton(self,
                                                    "",
                                                    self.chosenFormat,
                                                    FORMATS[0],
                                                    None,
                                                    430 + common_x,
                                                    320 + common_y)

        #Create a label for the WAV Radiobutton
        self.wavRadioLabel = cGUIf.get_TextLabel(self,
                                                 FORMATS[1],
                                                 self.radioButtonFont,
                                                 455 + common_x,
                                                 360 + common_y)

        #Create a Radiobutton for WAV
        self.wavRadiobutton = cGUIf.get_Radiobutton(self,
                                                    "",
                                                    self.chosenFormat,
                                                    FORMATS[1],
                                                    None,
                                                    430 + common_x,
                                                    360 + common_y)


        #Create a label for OGG
        self.oggRadioLabel = cGUIf.get_TextLabel(self,
                                                 FORMATS[2],
                                                 self.radioButtonFont,
                                                 455 + common_x,
                                                 400 + common_y)

        #Create a Radiobutton for OGG
        self.oggRadiobutton = cGUIf.get_Radiobutton(self,
                                                    "",
                                                    self.chosenFormat,
                                                    FORMATS[2],
                                                    None,
                                                    430 + common_x,
                                                    400 + common_y)

        #Create a label that says "Output File Location."
        self.outputFileLocationLabel = cGUIf.get_TextLabel(self,
                                                           "Output File Location",
                                                           self.labelFont,
                                                           210 + common_x,
                                                           450 + common_y)


        #Create an entry widget for the output file location
        self.outputFileLocationEntry = cGUIf.get_Entry(self,
                                                       self.entryFont,
                                                       220 + common_x,
                                                       500 + common_y)

        self.outputFileLocationEntry.configure(state = "readonly")

        #Create a button to allow the user to browse for a location for the file output
        self.outputFileLocationButton = cGUIf.get_Button(self,
                                                         "Browse",
                                                         self.ask_folder,
                                                         450 + common_x,
                                                         500 + common_y)
        

        #Create a button that allows the user to execute the convert operation
        self.convertButton = cGUIf.get_Button(self,
                                              "Convert",
                                              self.convert_command,
                                              260 + common_x,
                                              538 + common_y)

        #Font of the conversion button
        stylesin = ttk.Style()
        stylesin.configure("my.TButton",
                           font = (FONTS["helvetica"], 12))

        self.convertButton.configure(style = "my.TButton")


        #Create a label that says "Back" fir the back button
        self.backFont = font.Font(family = FONTS["cambria"], size = 12)
        self.backLabel = cGUIf.get_TextLabel(self,
                                             "Back",
                                             self.backFont,
                                             80 + common_x,
                                             504 + common_y)

        #Create a back button to go to the main Frame
        self.backButton = cGUIf.get_Button(self,
                                           "",
                                           self.switch_frames,
                                           30 + common_x,
                                           495 + common_y)
        
        self.backButton.configure(image = self.__pics["back_arrow"])


    
def main(): 
    """Run warning if run directly."""

    warning_message = "This script contains the code that builds the " \
                      + "audio conversion page of the FCA (File Converter App)." \
                      + "\n\nThis script should NOT be run DIRECTLY." \
                      + "\n\nPlease, import it in another script."

    cGUIf.show_warning("Import warning",warning_message)




if __name__ == "__main__": 
    main()
