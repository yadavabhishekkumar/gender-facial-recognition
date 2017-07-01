import cv2
from PIL import Image
import numpy as np 

vc = cv2.VideoCapture(0)

if vc.isOpened() and input('enter zero') == 0 : # try to get the first frame
    rval, frame1 = vc.read()

file1= "C:\\Users\\DELL\\codes\\Image\\gender\\joke.png"
cv2.imwrite(file1,frame1)
faceCascade = cv2.CascadeClassifier("C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml");
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load("C:\\Users\\DELL\\codes\\Image\\gender\\k.xml")	 
predict_image_pil = Image.open(file1).convert('L')
predict_image = np.array(predict_image_pil, 'uint8')
faces = faceCascade.detectMultiScale(predict_image) 
for (x, y, w, h) in faces:
 nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w]) 
 
  
 print (" Correctly Recognized as {}  with confidence {} ").format(nbr_predicted,conf) 
 
  
 cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
 cv2.waitKey(1000)


#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) in order to directly convert the frame in to a grayscale image .Advantage is you don't need to use cv2.imwrite and Image.open().convert()

vc.release()
del(vc)


