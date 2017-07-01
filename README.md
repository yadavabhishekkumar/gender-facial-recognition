# gender-facial-recognition
# About the Project
This project was done as a part of my summer project from home alone.I would especially like to thank Stackoverflow community for pulling me out of trouble every time that i encountered and Also the opensource community for OpenCV for such a simple explanation of complex ideas.  
# Collecting the datasets
In this project I have used 15 images of female celebrities and another 15 images of male celebrities for the purpose of training. Since they were downloaded from the google so they might not be available in uniform pixel size.That's why i wrote another script named "resize.py" for automatically adjusting the size of images present in the folder.                                                                       So first getting the images in correct size is important else you will encounter Error telling "unequal size of labels and images list".
# Training the model
Now comes the second phase which is training the model over the given datasets.I have used LBPH facerecognition technique.(LBPH- local binar patterns histogram).In this phase the name of the files are important(which should contain a label in the starting of name such as "1" in case of female  and "2" in case of male ).We will be extracting the labels from the name itself and simulatneously store the grayscale converted image in "images" list. And in the end we will save the trained Model in the form of XML file so that we don't have to run again and again the script "train.py".We can directly use this XML file for classification purpose.
# Testing the person
Finally comes the final phase in which image of person is taken using the webcam in your laptop.And this image is stored and tested using the saved model. And the final output will contain the Class to which image belongs and also the confidence percentage.                           TYPE 0 AND AFTER PRESSING THE ENTER KEY YOUR PHOTO WILL BE TAKEN and used for matching purpose.                       
# Requirements in terms of environment
The above project was performed in python language over compiler of version 2.7.12 in 64 bit  mode.
The most important component of this project was open source tool  "OpenCV" version 2.4.13.
You will also need to import Pillow.
# Possible errors 
There might be some technical difficulties (like in the installation of numpy or python) that you all may face so  just mail the error(how so ever trivial error may be) to my mail id: "ay70415" +"@gmail.com" . Just join them (Did this for security purpose from web crawlers)  
