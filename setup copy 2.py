
# Ideal Path
from slicer import *
import cv2

def fun(img,string,AddonString = ""):
    if (AddonString == "lower_" ):
        start = 0
        end = 52
    elif (AddonString == "upper_"):
        start = 52
        end = 104
    elif (AddonString == "special_"):
        start = 104
        end = 104 + len(string) * 2 -1

    index = 0

    for i in range(start,end,2):
        left = i * 9
        right = left + 9

        Crop_img = img[0 : 20 , left : right]
        cv2.imwrite("Media\Characterz\\"+AddonString+string[index]+".png",Crop_img)
        print(string[index])

        index += 1

def creator(img,path):
    string_lower = "abcdefghijklmnopqrstuvwxyz"
    string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # string_numbers = "0123456789"
    # string_special = "!\"#$%&'()*+,-./0123456789:;<=>?@"

    img = cv2.imread(path)
    img = Crop(img, up = 696 , down = 718 , left = 0 , right = 1250)
    # creator(img)

    fun(img, string_lower,AddonString = "lower_")
    fun(img, string_upper,AddonString = "upper_")
    
    # fun(img, string_special,AddonString = "special_")

def createBlank(img):
    char = 80 * 9
    charring = char + 9
    imgz = img[0:20,char:charring]
    show(imgz)  
    cv2.imwrite("Media\\Characters\\Blank.png",imgz)


if __name__ == '__main__':
    path = "Media//alpha.png"
    img = cv2.imread(path)


    # edit these to get the right coords for your terminal window where the c.c file was run
    UpperTerminalWindowCoords = 660
    LowerTerminalWindowCoords = 680
    LeftTerminalWindowCoords = 0
    RightTerminalWindowCoords = 800
    
    img_ = Crop(img, up = UpperTerminalWindowCoords , down = LowerTerminalWindowCoords , left = LeftTerminalWindowCoords , right = RightTerminalWindowCoords)
    
    createBlank(img_)
    creator(img,path)