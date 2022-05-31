from PIL import Image
import numpy as np
import csv
import cv2
import tracemalloc
import time 
import os 

def compression(st):
    data = []
    
    for j in range(len(st)):
        row = st[j]
        output = []
        n = len(row)
        i = 0
        while i < n:
            count = 1
            tmp = row[i]
            while (i < n - 1 and row[i] == row[i + 1]):
                count += 1
                i += 1
            i += 1

            if count>1:
                output.append('#'+str(count))
            output.append(str(tmp))
        data.append(output)

    return data



def decompression(st):
        data = []
        
        for j in range(len(st)):
            row = st[j]
            output = []
            n= len(row)
            i = 0
            
            while i < n:
                tmp = row[i]
                if tmp[0] == '#':
                    var = int(float(row[i+1]))
                    tmp = int(tmp[1:])
                    for j in range(tmp):
                        output.append(var)
                    i += 1
                else:
                    output.append(int(float(tmp)))
                i += 1
            
            data.append(output)
        
        return data

def runBenchmarks(directory, compression, decompression, output_dir):

    comp = []
    deco = []

    for path in os.listdir(directory):

        f = os.path.join(directory, path)  
        tracemalloc.start() 
        n = time.time() 
        im = np.array(Image.open(f).convert("L")) 
        image = compression(im) 
        current, peak = tracemalloc.get_traced_memory()  
        comp.append((f, time.time() - n, peak / 10**6, os.path.getsize(f)/ 10**6))  
        tracemalloc.stop() 
        tracemalloc.start() 
        n = time.time()
        newImage = decompression(image) 
        current, peak = tracemalloc.get_traced_memory() 
        deco.append((f, time.time() - n, peak / 10**6, os.path.getsize(f)/ 10**6)) 
        cv2.imwrite(os.path.join(output_dir, path) , np.array(newImage))  
        tracemalloc.stop() 

    with open("compression_benchmarks_RunLength.csv", "w") as f: 
        writer = csv.writer(f)
        writer.writerow(["path", "time", "memory", "filesize"])
        for line in comp:
            writer.writerow(line)
    with open("decompression_benchmarks_RunLength.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["path", "time", "memory", "filesize"])
        for line in deco:
            writer.writerow(line)



route = r"C:\Users\DELL\Desktop\Datos y Algoritmos\Proyecto\codigo\pythonProject\test"
output = r"C:\Users\DELL\Desktop\Datos y Algoritmos\Proyecto\codigo\pythonProject\RunLengthOutput"

# runBenchmarks(route, compression, decompression, output)



