# write a  code to cut the image for the given coordinates
# and save it in the same folder with the name of the image
import cv2

def show(img):
    '''
    --------------------------------------
    Shows the Image
    --------------------------------------
    @Params: img: image to be shown
    
    @Returns: None
    '''
    cv2.imshow('image', img)
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


if __name__ == '__main__':
    path = r"Media\task5step4.png"
    img = cv2.imread(path)
    # test(img)
