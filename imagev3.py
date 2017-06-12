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




i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)
	
'''
threshold(iar2)
threshold(iar3)
threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)

ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)

ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)

ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()




'''