import numpy as np 
import os
import cv2

from PIL import Image

faceCascade = cv2.CascadeClassifier("C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml");

recognizer = cv2.createLBPHFaceRecognizer()

def get_images_and_labels(path): 
	# Append all the absolute image paths in a list image_paths 
# We will not read the image with the .sad extension in the training set 
# Rather, we will use them to test our accuracy of the training 
 image_paths = [os.path.join(path, f) for f in os.listdir(path) ] 
# images will contains face images
 images = [] 
 
 # labels will contains the label that is assigned to the image
 labels = [] 
 for image_path in image_paths: 
  # Read the image and convert to grayscale 
		image_pil = Image.open(image_path).convert('L') 
		# Convert the image format into numpy array 
		image = np.array(image_pil, 'uint8') 
		# Get the label of the image 
		nbr = int(os.path.split(image_path)[1].split(".")[0][0])
		
		# Detect the face in the image 
		faces = faceCascade.detectMultiScale(image)
		# If face is detected, append the face to images and the label to labels 
		for (x, y, w, h) in faces:
		  images.append(image[y: y + h, x: x + w])
		labels.append(nbr)
		print "labels length:  "
		print len(labels)
		print "images length:   "
		print len(images)
		cv2.startWindowThread()
		cv2.namedWindow("preview")
		
		cv2.imshow("preview", image[y: y + h, x: x + w]) 
		cv2.waitKey(1) 
			# return the images list and labels list
 return images, labels



path ="C:\\Users\\DELL\\codes\\Image\\gender\\face" 
	  # The folder yalefaces is in the same folder as this python script
	   # Call the get_images_and_labels function and get the face images and the
	    # corresponding labels
images, labels = get_images_and_labels(path) 
cv2.destroyAllWindows() 
		 
		 #Perform the training
recognizer.train(images, np.array(labels))
recognizer.save("C:\\Users\\DELL\\codes\\Image\\gender\\k.xml") 
