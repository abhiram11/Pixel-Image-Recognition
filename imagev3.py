from collections import Counter
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce

def createExamples():
	numberArrayExamples = open('numArEx.txt','a') #a refers to append
	numbersWeHave = range(0,10) #0 to 9
	versionsWeHave = range(1,10) #1 to 9

	for eachNum in numbersWeHave:
		for eachVersion in versionsWeHave:
			print( str(eachNum)+'.'+str(eachVersion))
			imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVersion)+'.png'
			ei = Image.open(imgFilePath) #example image
			eiar = np.array(ei)
			eiar1 = str(eiar.tolist())


			#to show which image the experiment image corresponds to
			lineToWrite = str(eachNum)+'::'+eiar1+'\n'
			numberArrayExamples.write(lineToWrite)





createExamples()


def threshold(imageArray): #VALUE above threshold will be black and below will be white
							#aise hi kuch type ka
	balanceArray = []
	newArray = imageArray

	for eachRow in imageArray:
		for eachPixel in eachRow:
			avgNum = reduce(lambda x,y: x+y,eachPixel[:3])/len(eachPixel[:3])#excluding alpha
			balanceArray.append(avgNum)

			'''print (eachPixel)
			time.sleep(5)'''
	balance = reduce(lambda x,y: x+y,balanceArray[:3])/len(balanceArray[:3])
	
	for eachRow in newArray:
		for eachPixel in eachRow:
			if reduce(lambda x,y: x+y,eachPixel[:3])/len(eachPixel[:3]) > balance:
				eachPixel[0] = 255
				eachPixel[1] = 255
				eachPixel[2] = 255
				eachPixel[3] = 255
			else:
				eachPixel[0] = 0
				eachPixel[1] = 0
				eachPixel[2] = 0
				eachPixel[3] = 255

	return newArray



def whatNumIsThis(filePath):
	matchedArray = [] #matches will be stored in this array
	#this is basic idea of neural networks
	loadExamples = open('numArEx.txt','r').read()
	loadExamples = loadExamples.split('\n')

	i = Image.open(filePath)
	iar = np.array(i)
	iarl = iar.tolist()
	
	inQuestion = str(iarl)

	for eachExample in loadExamples: 
		if len(eachExample)>3: #to avoid blank lines
			splitEx = eachExample.split('::')
			currentNum = splitEx[0] #first element
			currentArray = splitEx[1] #for whole array of item
#to compare pixel to pixel
			eachPixEx = currentArray.split('],') #to split every 4 element waali array

			eachPixINQues = inQuestion.split('],')
			

			#while loop cuz we dont know how long the loop will run
			x=0;
			while x<len(eachPixEx):
				if eachPixEx[x] ==  eachPixINQues[x]: #x index
					matchedArray.append(int(currentNum)) #append that integer to the empty matched array

				x+=1
	
	print(matchedArray)					

	x = Counter(matchedArray) #eg. for [1,2,3,1,1,2,1,3,4] counter will give output {1:4,2:2,3:2,4:1}
	print (x)

whatNumIsThis('images/test.png') #draw any number like digit and save it as test.png in this folder and run the code..
#the counter function will show the number the test image is most probably related to
