import cv2
import cv2.cv as cv
import numpy as np

# to extract from a particular file 
print(cv2.__version__)
vidcap = cv2.VideoCapture('sqr15ptop.wmv') # enter the filenmame
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  count += 1




fid=open("text.txt","w") #to store the data in a file
a=80	#these are the starting values of max and min radius
b=100   #max radius
k=1

while k<101:
	count1=0
	count2=0
	img = cv2.imread('frame'+str(k)+'.jpg',0)
	crop_img = img[1052:1316, 1222:1458] #crop out a particular area to the image if you need
	cimg = cv2.cvtColor(crop_img,cv2.COLOR_GRAY2BGR)
	circles = cv2.HoughCircles(crop_img,cv.CV_HOUGH_GRADIENT,1,10,param1=50,param2=36,minRadius=a,maxRadius=b)
	try:
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
    			# draw the outer circle
    			cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2) #i[0,1,2] is x,y,r
    			cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
			count1+=i[0]
			count2+=1
		print >> fid, count1*1.0/count2	,"\t", k*0.3
		print count1*1.0/count2	,"\t", k, count2
		k+=1
	except:	#because expanding circle##
		a+=1
		b+=1
		print "exception",k
		k+=1
	cv2.imshow('detected circles',cimg)
	cv2.resizeWindow('detected circles', 200,200)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


#now an intelligent particle tracking code if the python Houghcircle is not good enough. Further this method will be useful if the shape is not a circle but something else
#For a bacteria of a peculiar shape this can be used to track the centroid or the boundary of the bacteria.


import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
fid=open('final.txt','w')

kk=1
while kk<=100:
	im = cv2.imread('frame'+str(kk)+'.jpg')
	crop_img = im[1000:1400, 1200:1500]
	imCopy = crop_img.copy()
	imgray=cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,55,255,cv2.THRESH_BINARY_INV)
	#plt.imshow(thresh,'gray')
	#plt.show()
	contours, hierarchy =  cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(imCopy,contours,-1,(0,255,0))
	#cv2.imshow('draw contours',imCopy)
	#cv2.waitKey(0)
	#M=cv2.moments(contours[0])
	#print M
	import cv2.cv as cv
	#hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]]
	#hull = cv.convexHull(contours[0])
	#import cv2.cv as cv
	(x,y),radius = cv2.minEnclosingCircle(contours[0])
	center = (int(x),int(y))
	radius = int(radius)
	cv2.circle(thresh,center,radius,(0,255,0),2)
	#print center
	count=1
	x_position=[]
	y_position=[]
	for a in range(0,len(contours)):
		for b in range(0,len(contours[a])):
			x_position.append(contours[a][b][0][0])
			y_position.append(contours[a][b][0][1])
	print np.mean(x_position),np.mean(y_position),kk	
	print >> fid,np.mean(x_position),np.mean(y_position),kk	
	#print len(contours)
	#print len(contours[0])
	#print contours[0]#[1][0][0]
	#thresh is the name of the image
	kk+=1
	
