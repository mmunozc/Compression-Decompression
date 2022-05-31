from PIL import Image
import numpy as np

im = np.array(Image.open("Rosa.jpg").convert("L")) 
print(im.shape)


factor = 2
x = im.shape[0]//factor
y = im.shape[1]//factor
output = []

print(im)

for i in range(x):
    row = []
    for j in range(y):
        row.append(im[i*factor][j*factor])
    output.append(row)

outputImage = Image.fromarray(np.array(output), "L")
outputImage.save("CompressionRosa.jpg")


def imageScallingCompression(img):

    factor = 2
    x = im.shape[0]//factor
    y = im.shape[1]//factor
    output = []

    for i in range(x):
        row = []
        for j in range(y):
            row.append(img[i*factor][j*factor])
        output.append(row)
    
    return output


    