import cv2
from random import randrange

#load some pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an img to detect faces in
#img = cv2.imread(r"C://Users//rozer//OneDrive//Resimler//friends.jpg")

#to capture video from webcam, eğer 0 verirsen kendi webcam ine bağlanırsın, name girersen o mp4 çalışır
webcam = cv2.VideoCapture(0)

#iterate forever over frames
while True:
    ###Read the current frame
    successful_frame_read, frame = webcam.read()

    #Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
    #draw rectangles around the faces
        cv2.rectangle(frame, (x, y) ,(x+w, y+h), (0, 255,0), 5)



    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)
    
    
    ####Stop if Q key is pressed
    if key==81 or key==113:
        break

####release the videocapture obj
webcam.release()
print("code completed")
"""
#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

for (x, y, w, h) in face_coordinates:
#draw rectangles around the faces
    cv2.rectangle(img, (x, y) ,(x+w, y+h), (randrange(256), randrange(256),randrange(256)), 5)



#print(face_coordinates)

cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()
print("code completed")
"""