# write a  code to cut the image for the given coordinates
# and save it in the same folder with the name of the image
import cv2

def show(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)



def CoordinateData(dictionaryMode = False):
    '''
    --------------------------------------
    Sets Up the Coordinates for the Parts
    --------------------------------------
    @Params: None

    @Returns: tabUp,tabDow, winLeft, winRight, winUp, winDow
    
    '''
    coords_tabs = { "tabs-upper" : 70 , "tabs-lower" : 110 , "window-left" : 25 , "window-right" : 760 , "window-bottom" : 545, "window-top" : 26 }
    if dictionaryMode:
        return coords_tabs
    else:
        tabUp,tabDow, winLeft, winRight, winUp, winDow = coords_tabs["tabs-upper"],coords_tabs["tabs-lower"], coords_tabs["window-left"], coords_tabs["window-right"], coords_tabs["window-top"], coords_tabs["window-bottom"]
        return tabUp,tabDow, winLeft, winRight, winUp, winDow

def Tab(img,showing = False):
    '''
    --------------------------------------
    Shows the Tabs
    --------------------------------------
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]

    @Returns: Crop_img: Cropped image
    '''
    tabUp,tabDow, winLeft, winRight, winUp, winDow = CoordinateData()
    Crop_img = img[tabUp : tabDow , winLeft : winRight]
    if showing:
        show(Crop_img)
    return Crop_img
def Title(img,showing = False):
    '''
    --------------------------------------
    Shows the Title
    --------------------------------------
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]

    @Returns: Crop_img: Cropped image
    '''
    tabUp,tabDow, winLeft, winRight, winUp, winDow = CoordinateData()
    Crop_img = img[winUp : tabUp , winLeft : winRight]
    if showing:
        show(Crop_img)
    return Crop_img
def Window(img,showing = False):
    '''
    --------------------------------------
    Shows the Window
    --------------------------------------
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]

    @Returns: Crop_img: Cropped image
    '''
    tabUp,tabDow, winLeft, winRight, winUp, winDow = CoordinateData()
    Crop_img = img[tabDow : winDow , winLeft : winRight]
    if showing:
        show(Crop_img)
    return Crop_img
# Crop the image
def Crop(img,showing = False , up = 0 , down = 20 , left = 0 , right = 0):
    '''
    --------------------------------------
    Crops the Image
    --------------------------------------
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]
    @Params: up: upper bound of the image [Default: 0]
    @Params: down: lower bound of the image [Default: 0]
    @Params: left: left bound of the image [Default: 0]
    @Params: right: right bound of the image [Default: 0]
    
    @Returns: Crop_img: Cropped image
    '''
    Crop_img = img[up : down , left : right]
    if showing:
        show(Crop_img)
    return Crop_img
    
def StanderdizeLook(img,showing = False):
    '''
    --------------------------------------
    Standerdizes the Image
    --------------------------------------
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]

    @Returns: Image
    '''
    tabUp,tabDow, winLeft, winRight, winUp, winDow = CoordinateData()
    img = Crop(img,showing = showing , up = winUp , down = winDow , left = winLeft , right = winRight)
    return img

def GetLines(img,line = 1,CharacterStart = 0,CharacterEnd = -1,showing = False):
    '''
    --------------------------------------
    Gets the Lines from the Image
    --------------------------------------
    @Params: img: image to be Cropped
    @Params: showing: shows image (True/False) [Default: False]

    @Returns: Image
    '''
    line = line - 1 # to make it zero based
    
    coords = CoordinateData(dictionaryMode=True)

    if CharacterEnd <= 0  :
        CharacterEnd = 73
    if CharacterStart < 0 :
        CharacterStart = 0
    # Swapping the values if CharacterStart > CharacterEnd
    if CharacterStart > CharacterEnd:
        CharacterStart,CharacterEnd = CharacterEnd,CharacterStart
    if CharacterStart == CharacterEnd:
        CharacterEnd = CharacterStart + 1

    LineHeightTop = line * 20
    LineHeightBottom =LineHeightTop + 20
    
    CharacterWidthLeft = coords["window-left"] + (CharacterStart) * 9
    CharacterWidthRight =  coords["window-left"] + (CharacterEnd) * 9

    Cropping = Crop(img,showing = showing , up = coords["tabs-lower"] + LineHeightTop, down = coords["tabs-lower"] + LineHeightBottom , left = CharacterWidthLeft, right = CharacterWidthRight)
    return Cropping


def fun(img,string,AddonString = ""):
    if (AddonString == "_lower" ):
        start = 0
        end = 52
    elif (AddonString == "_upper"):
        start = 52
        end = 104
    elif (AddonString == "_number"):
        start = 104
        end = 122

    index = 0

    for i in range(start,end,2):
        left = i * 9
        right = left + 9

        Crop_img = img[0 : 20 , left : right]
        cv2.imwrite("Media\Characters\\"+string[index]+AddonString+".png",Crop_img)
        print(string[index])
        index += 1

def creator(img,path):
    string_lower = "abcdefghijklmnopqrstuvwxyz"
    string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string_numbers = "123456789"

    img = cv2.imread(path)
    img = Crop(img, up = 696 , down = 718 , left = 0 , right = 1250)
    # creator(img)

    fun(img, string_lower,AddonString = "_lower")
    fun(img, string_upper,AddonString = "_upper")
    fun(img, string_numbers,AddonString = "_number")

if __name__ == '__main__':
    path = r"Media\task5step4.png"
    # path = "Media//alpha.png"
    img = cv2.imread(path)
    # creator(img,path)
    for i in range(0,12,1):
        GetLines(img, line = 2,CharacterStart = i,CharacterEnd = i+1,showing = True)
           