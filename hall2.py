import cv2
import numpy as np
import time


path = "calligraphies/"
path2 = "fronts/"

img =  cv2.imread(path2 + "front.jpg",0)
img1 =  cv2.imread(path2 + "front3.jpg",0)
img21 = cv2.imread(path2 + "front31.jpg",0)
img22 = cv2.imread(path2 + "front32.jpg",0)
img23 = cv2.imread(path2 + "front33.jpg",0)
img24 = cv2.imread(path2 + "front34.jpg",0)
img25 = cv2.imread(path2 + "front35.jpg",0)
index = 0

img211 = cv2.imread(path + "batarde.jpg",0)
img212 = cv2.imread(path + "cadel.jpg",0)
img213 = cv2.imread(path + "fraktur.jpg",0)
img214 = cv2.imread(path + "gothic.jpg",0)
img215 = cv2.imread(path + "lombardic.jpg",0)

img221 = cv2.imread(path + "humanist miniscule.jpg",0)
img222 = cv2.imread(path + "italics.jpg",0)
img223 = cv2.imread(path + "rotunda.jpg",0)

img231 = cv2.imread(path + "imperial.jpg",0)

img241 = cv2.imread(path + "copperplate.jpg",0)
img242 = cv2.imread(path + "copperplate capitals.jpg", 0)

img251 = cv2.imread(path + "rustic.jpg",0)
img252 = cv2.imread(path + "uncial.jpg",0)

def rec_maker(image, i):

    for j in range(i):
        cv2.rectangle(image, (100, 100*(1+j)), (600 , 200+ 100*j), (0, 55, 75), 3)

def font_add(image):

    row,col = image.shape
    print(row,col)
    blank_image = np.zeros((row + 30,col), np.uint8)
    print(blank_image.shape)
    blank_image[:][:] = 255

    blank_image[:row][:col] = image[:][:]

    image = blank_image

    font                   = cv2.FONT_HERSHEY_PLAIN
    bottomLeftCornerOfText = (10,row+20)
    fontScale              = 1
    fontColor              = (0,0,0)
    lineType               = 2

    cv2.putText(image,'Press \'q\' to close window',
        bottomLeftCornerOfText,
        font,
        fontScale,
        fontColor,
        lineType)

    return image

def changer(event,x,y,flags,param):

    global index
    #print(x,y)
    if event == cv2.EVENT_LBUTTONDOWN:

        if index == 0:
            cv2.imshow('image',img1)
            index = 1

        else:
            if (x > 100 and x < 600) and (y > 100 and y < 200):
                if index == 1:
                    cv2.imshow('image', img21)
                    index = 21
                elif index == 21:
                    cv2.imshow('image1',img211)
                elif index == 22:
                    cv2.imshow('image1',img221)
                elif index == 23:
                    cv2.imshow('image1',img231)
                elif index == 24:
                    cv2.imshow('image1',img241)
                elif index == 25:
                    cv2.imshow('image1',img251)

            elif (x > 100 and x < 600) and (y > 200 and y < 300):
                if index == 1:
                    cv2.imshow('image', img22)
                    index = 22
                elif index == 21:
                    cv2.imshow('image1', img212)
                elif index == 22:
                    cv2.imshow('image1', img222)
                elif index == 24:
                    cv2.imshow('image1', img242)
                elif index == 25:
                    cv2.imshow('image1', img252)
            elif (x > 100 and x < 600) and (y > 300 and y < 400):
                if index == 1:
                    cv2.imshow('image', img23)
                    index = 23
                elif index == 21:
                    cv2.imshow('image1', img213)
                elif index == 22:
                    cv2.imshow('image1', img223)
            elif (x > 100 and x < 600) and (y > 400 and y < 500):
                if index == 1:
                    cv2.imshow('image', img24)
                    index = 24
                elif index == 21:
                    cv2.imshow('image1', img214)
            elif (x > 100 and x < 600) and (y > 500 and y < 600):
                if index == 1:
                    cv2.imshow('image', img25)
                    index = 25
                elif index == 21:
                    cv2.imshow('image1', img215)

#win_name = cv2.namedWindow('image')


if __name__ == "__main__":

    cv2.imshow('image',img)
    cv2.setMouseCallback('image', changer)
    #k = cv2.waitKey(1)
    rec_maker(img1,5)
    rec_maker(img21, 5)
    rec_maker(img22, 3)
    rec_maker(img23, 1)
    rec_maker(img24, 2)
    rec_maker(img25, 2)

    img211 = font_add(img211)
    img212 = font_add(img212)
    img213 = font_add(img213)
    img214 = font_add(img214)
    img215 = font_add(img215)
    img221 = font_add(img221)
    img222 = font_add(img222)
    img223 = font_add(img223)
    img231 = font_add(img231)
    img241 = font_add(img241)
    #img242 = font_add(img242)
    img251 = font_add(img251)

    while True:

        k = cv2.waitKey(0)
        print(k)
        if k == 27:

            cv2.destroyAllWindows()
            exit()

        elif k== 98:
            index = 1
            cv2.imshow('image', img1)
        elif k==113:
            cv2.destroyWindow("image1")

