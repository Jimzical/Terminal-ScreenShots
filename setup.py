
# Ideal Path
from slicer import *
import cv2
import numpy as np #TODO: Remove this later on

def fun(img,string,AddonString = ""):
    if (AddonString == "lower_" ):
        start = 0
        end = 52
    elif (AddonString == "upper_"):
        start = 52
        end = 104
    elif (AddonString == "number_"):
        start = 104
        end = 104 + len(string) * 2 -1

    index = 0

    for i in range(start,end,2):
        left = i * 9
        right = left + 9

        Crop_img = img[0 : 19 , left : right]
        cv2.imwrite("Media\Characters\\"+AddonString+string[index]+".png",Crop_img)
        print(string[index])

        index += 1

def creator(img,path):
    string_lower = "abcdefghijklmnopqrstuvwxyz"
    string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string_numbers = "0123456789"
    # string_special = "!\"#$%&'()*+,-./0123456789:;<=>?@"

    img = cv2.imread(path)
    img = Crop(img, up = 696 , down = 718 , left = 0 , right = 1250)

    fun(img, string_lower,AddonString = "lower_")
    fun(img, string_upper,AddonString = "upper_")
    
    # fun(img, string_special,AddonString = "special_")

def createBlank(img):
    char = 80 * 9
    charring = char + 9
    imgz = img[0:19,char:charring]
    show(imgz)  
    cv2.imwrite("Media\\Characters\\Blank.png",imgz)

def saveUser(img,characterLength = 27):
    img = Crop(img, up = 0 , down = 20 , left = 0 , right = characterLength * 9)
    
    # clear all files in folder Media\User
    # files = os.listdir(r"Media\User")
    # for file in files:
    #     os.remove("Media\\User\\"+file)

    # save all the characters
    for i in range(0,characterLength,1):
        left = i * 9
        right = left + 9
        Crop_img = img[0 : 20 , left : right]
        show(Crop_img)
        saveLocation = r"Media\User\{i}.png".format(i = str(i))
        cv2.imwrite(saveLocation,Crop_img)

    show(img)
    # cv2.imwrite("Media\\Characters\\Username.png",img)
def BuildUserImage():
    files = os.listdir(r"Media\User")
    img = cv2.imread("Media\\User\\0.png")
    for i in range(1,len(files),1):
        path = r"Media\User\{i}.png".format(i = str(i))
        img_ = cv2.imread(path)
        img = np.concatenate((img,img_),axis = 1)
    return img

def NewUsername(img,characterLength):  
    show(img) 
    newImage = Crop(img, up = 0 , down = 20 , left = 0 , right = characterLength * 9)
    show(newImage)
    print(newImage.shape)
    cv2.imwrite("Media\\Characters\\Username.png",newImage)
if __name__ == '__main__':
    path = "Media//alpha.png"  # path where the c.c code was run originally
    
    # # img = cv2.imread(path)
    # # just for testing
    Userpath =r"Media\task5step4.png"
    
    img = cv2.imread(path)
    img = Window(img)

    Userimg = cv2.imread(Userpath)
    Userimg = Window(Userimg)
    UsernameLenght = 27 #will vary for user to user

    NewUsername(Userimg,UsernameLenght)
    # saveUser(Userimg,characterLength = UsernameLenght)
    # Userimg = BuildUserImage()
    # show(Userimg)

    # UpperTerminalWindowCoords = 660
    # LowerTerminalWindowCoords = 680
    # LeftTerminalWindowCoords = 0
    # RightTerminalWindowCoords = 800

    # img_ = Crop(img, up = 660 , down = 680 , left = 0 , right = 800)
    # img_ = Crop(img, up = UpperTerminalWindowCoords , down = LowerTerminalWindowCoords , left = LeftTerminalWindowCoords , right = RightTerminalWindowCoords)
    
    # createBlank(img_)
    # creator(img,path)
   
    