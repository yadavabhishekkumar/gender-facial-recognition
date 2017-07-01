from PIL import Image

baseheight = 300
#in range excludes the upper limit no. but includes the lower limit no.
for i in range(1,16):       #here you need to enter the no. of image file which in my case was 15  so the upper limit should be 16
	filename='C:\\Users\\DELL\\codes\\Image\\gender\\1('+str(i)+').jpg'        #here you need to make modifications as per your file path
#and also for resizing the male actors image you need to replace "1" with "2" as the name of male actors image starts with "2"
	img = Image.open(filename)
	hpercent = (baseheight / float(img.size[1]))
	wsize = int((float(img.size[0]) * float(hpercent)))
	img = img.resize((wsize, baseheight),Image.ANTIALIAS)
	filename2='C:\\Users\\DELL\\codes\\Image\\gender\\1('+str(i)+').jpg'
	img.save(filename2)
