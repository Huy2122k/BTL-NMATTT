''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc                       

Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18    

'''

import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x,y,w,h) in faces:

    #     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     

    cv2.imshow('hướng mặt lên trên rồi bấm q', img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break


# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x,y,w,h) in faces:

    #     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
    count += 1

        # Save the captured image into the datasets folder
    cv2.imwrite("dataset/user/User." + "up" + '.' + str(count) + ".jpg", img)

    cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 5: # Take 5 face sample and stop video
         break



while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x,y,w,h) in faces:

    #     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     

    cv2.imshow('hướng mặt xuống dưới rồi bấm q', img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break


count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x,y,w,h) in faces:

    #     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
    count += 1

        # Save the captured image into the datasets folder
    cv2.imwrite("dataset/user/User." + "down" + '.' + str(count) + ".jpg", img)

    cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 5: # Take 5 face sample and stop video
         break


while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x,y,w,h) in faces:

    #     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     

    cv2.imshow('hướng mặt sang trái rồi bấm q', img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x,y,w,h) in faces:

    #     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
    count += 1

        # Save the captured image into the datasets folder
    cv2.imwrite("dataset/user/User." + "left" + '.' + str(count) + ".jpg", img)

    cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 5: # Take 5 face sample and stop video
         break

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x,y,w,h) in faces:

    #     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     

    cv2.imshow('hướng mặt sang phải rồi bấm q', img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break


count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x,y,w,h) in faces:

    #     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
    count += 1

        # Save the captured image into the datasets folder
    cv2.imwrite("dataset/user/User." + "right" + '.' + str(count) + ".jpg", img)

    cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 5: # Take 5 face sample and stop video
         break


# Do a bit of cleanup
cam.release()
cv2.destroyAllWindows()


print("\n Đã nhập dataset xong! bấm enter để train")



