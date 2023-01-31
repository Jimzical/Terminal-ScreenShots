
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
    string_special = "!\"#$%&'()*+,-./0123456789:;<=>?@"

    img = cv2.imread(path)
    img = Crop(img, up = 696 , down = 718 , left = 0 , right = 1250)
    # creator(img)

    fun(img, string_lower,AddonString = "lower_")
    fun(img, string_upper,AddonString = "upper_")
    fun(img, string_special,AddonString = "special_")

if __name__ == '__main__':
    path = "Media//alpha.png"
    img = cv2.imread(path)

    img = GetLines(img,showing = True,line=2,CharacterStart=0,CharacterEnd=73)
    creator(img,path)