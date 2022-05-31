from PIL import Image
import numpy as np
from collections import deque
import tracemalloc
import time 
import os 
import csv
import cv2

from imageScalling import imageScallingCompression
from imageScalling import imageScallingDecompression
from runLength import compression
from runLength import decompression

directory =  r"C:\Users\DELL\Desktop\Datos y Algoritmos\Proyecto\codigo\pythonProject\test"
l = []
# print(os.listdir(directory))
for path in [file for file in os.listdir(directory) if file.endswith(".jpg")]:
    im = np.array(Image.open(os.path.join(directory, path)).convert("L")) #Cargo la imagen a un arreglo de numpy
    with open(os.path.join(directory, "output2", path), "w") as f:
        writer = csv.writer(f)
        for row in im:
            writer.writerow(row.tolist())
    image = imageScallingCompression(im) # realizo algoritmo compresion
    
    c2 = compression(image)
    d2 = os.path.join(directory, "output", path)
    with open(d2, "w") as f:
        writer = csv.writer(f)
        for row in image:
            writer.writerow(row)
    l.append((os.path.getsize(os.path.join(directory, "output2", path)), os.path.getsize(os.path.join(directory, "output", path))))

with open("compression.csv", "w") as f:
    writer = csv.writer(f)
    for line in l:
        writer.writerow(line)









