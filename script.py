#save it in the image folder...

from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np

i = Image.open('images/dot.png')
im = Image.open('images/numbers/y0.4.png')
iar = np.asarray(im) #image array or numpy array
#3d array = array within an array within an array for image's : row,column,pixel

print (iar) #prints array of the form [red, green, blue, alpha = transparency/solidity]

plt.imshow(iar)
plt.show()

