# write a  code to cut the image for the given coordinates
# and save it in the same folder with the name of the image
import cv2
import os
import numpy as np

def show(img):
    '''
    --------------------------------------
    Shows the Image
    --------------------------------------
    @Params: img: image to be shown
    
    @Returns: None
    '''
    cv2.imshow('Edit', img)
    cv2.waitKey(0)

def CoordinateData(dictionaryMode = False):
    '''
    --------------------------------------
    Sets Up the Coordinates for the Parts
    --------------------------------------
    @Params: dictionaryMode: returns a dictionary of the coordinates (True/False) [Default: False]

    @Returns: tabUp,tabDow, winLeft, winRight, winUp, winDow
    
    '''

    # TODO: Read this from a json file later on for better maintainability

    coords_tabs = { "tabs-upper" : 70 , "tabs-lower" : 110 , "window-left" : 25 , "window-right" : 760 , "window-bottom" : 545, "window-top" : 26 }
    if dictionaryMode:
        return coords_tabs
    else:
        tabUp,tabDow, winLeft, winRight, winUp, winDow = coords_tabs["tabs-upper"],coords_tabs["tabs-lower"], coords_tabs["window-left"], coords_tabs["window-right"], coords_tabs["window-top"], coords_tabs["window-bottom"]
        return tabUp,tabDow, winLeft, winRight, winUp, winDow

# Crop the image
def Crop(img,showing = False , up = 0 , down = 20 , left = 0 , right = 9):
    '''
    --------------------------------------
    Crops the Image
    --------------------------------------
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]
    @Params: up: upper bound of the image [Default: 0]
    @Params: down: lower bound of the image [Default: 20]
    @Params: left: left bound of the image [Default: 0]
    @Params: right: right bound of the image [Default: 9]
    
    @Returns: Crop_img: Cropped image
    '''
    Crop_img = img[up : down , left : right]
    if showing:
        show(Crop_img)
    return Crop_img


def GetLines(img,line = 1,CharacterStart = 0,CharacterEnd = -1,showing = False):
    '''
    --------------------------------------
    Gets the Lines from the Image
    --------------------------------------
    ## NOTE: This Fuction should be used directly with the read image
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]

    @Returns: Image
    '''
    line = line - 1 # to make it zero based
    
    coords = CoordinateData(dictionaryMode=True) #getting the coordinates

    # Setting the default values
    if CharacterEnd <= 0  :
        CharacterEnd = 73
    if CharacterStart < 0 :
        CharacterStart = 0

    #  Some Error Handling
    if CharacterStart > CharacterEnd:
        CharacterStart,CharacterEnd = CharacterEnd,CharacterStart
    if CharacterStart == CharacterEnd:
        CharacterEnd = CharacterStart + 1

    LineLocation = line * 20
    LineHeight = 20
    # LineHeightBottom =LineHeightTop + 20
    
    CharacterWidthLeft = coords["window-left"] + (CharacterStart) * 9
    CharacterWidthRight =  coords["window-left"] + (CharacterEnd) * 9

    Cropping = Crop(img,showing = showing , up = coords["tabs-lower"] + LineLocation, down = coords["tabs-lower"] + LineLocation + LineHeight  , left = CharacterWidthLeft, right = CharacterWidthRight)
    return Cropping

def test(img = None,letters = 20):
    '''
    --------------------------------------
    Testing the GetLines Function
    --------------------------------------
    @Params: img: image to be Cropped

    @Returns: None
    '''
    for i in range(0,letters,1):
            GetLines(img, line = 2,CharacterStart = i,CharacterEnd = i+1,showing = True)

def GetAlpha():
    
    # check if folder exists
    if not os.path.exists("Media\Characters"):
        os.mkdir("Media\Characters")
    # list folder contents
    files = os.listdir("Media\Characters")
    # save the conntents in a dict wiht the name as key and the image as value
    characters = {}

    for file in files:
        if file == 'Username.png':
            characters["Username"] = cv2.imread("Media\Characters\\" + file)
        if file == 'Blank.png':
            characters["Blank"] = cv2.imread("Media\Characters\\" + file)
        else:
            characters[file[0]] = cv2.imread("Media\Characters\\" + file)
    return characters


def TextConstructor(string="Hello World",overwrite = True,FirstLine = False):
    # TODO: Add Spaces
    # TODO: Add New Lines Functionality

    # TODO: Add a check to see if the string is too long
    # TODO: Add a check to see if the string is too short
    # TODO: Add a check to see if the string is empty

    AlphaBeth = GetAlpha()

    if FirstLine:
        text = AlphaBeth["Username"]
        if string[0] == " ":
            text = np.concatenate((text,AlphaBeth["Blank"]),axis=1)
        else:
            print(text.shape)
            print(AlphaBeth[string[0]].shape)
            text = np.concatenate((text,AlphaBeth[string[0]]),axis=1)

    elif string[0] == " ":
        text = AlphaBeth["Blank"]
    else:
        text = AlphaBeth[string[0]]

    for letter in range(0,len(string)-1):
        # print(string[letter+1])
        if string[letter+1] == " ":
            text = cv2.hconcat([text,AlphaBeth["Blank"]])
        else:
            text = cv2.hconcat([text,AlphaBeth[string[letter+1]]])
    return text


def Window(img,showing = False):
    '''
    --------------------------------------
    Shows the Window
    --------------------------------------
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]

    @Returns: Crop_img: Cropped image
    '''

    # TODO: Add a non tab version as well
    tabUp,tabDow, winLeft, winRight, winUp, winDow = CoordinateData()
    Crop_img = img[tabDow : winDow , winLeft : winRight]
    if showing:
        show(Crop_img)
    return Crop_img

def LineBuilder(img,showing = False,line = 1,string = 'hi',overwrite = False):
    '''
    --------------------------------------
    Builds the Text
    --------------------------------------

    @Returns: Crop_img: Cropped image
    '''

    if line == 1:
        FirstLine = True
    else:
        FirstLine = False

    text = TextConstructor(string,overwrite = overwrite,FirstLine = FirstLine)
    line = line - 1 # to make it zero based
    Yoffset = 2
    CharacterLenght = len(string) * 9 

    LineOffset = line * 20 - Yoffset
    img[4+LineOffset:20+LineOffset ,0:CharacterLenght ] = text[4:20 ,0:CharacterLenght]
    if showing:
        show(img)
    return img

def OverWrite(string):
    space = " " * (81 - len(string))
    # print(len(string))
    string = string + space
    # print(len(space))
    return string

def tempFix( img,string = "hi",overwrite = False,showing = False,line = 1):
    if overwrite:
        string = OverWrite(string)

    LineBuilder(img,showing = showing,line = line,string = string,overwrite = True) 


if __name__ == '__main__':
    path = r"Media\task5step4.png"
    img = cv2.imread(path)
    img = Window(img)
    string = 'LoL these are just random numbers idk any real commands here'


    # a = GetAlpha()
    # print("USER:",a['Username'].shape)
    # print("BLANK:",a['Blank'].shape)
    # print("A:",a['A'].shape)

    tempFix(img,string = string , overwrite=True , line=1, showing=True)
    # LineBuilder(img,showing = True,line = 2,string = string,overwrite = True)
    
    
    
