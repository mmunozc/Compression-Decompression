from PIL import Image
import numpy 
from collections import deque

im = numpy.array(Image.open("CompressionRosa.jpg").convert("L")) 
print (im.shape)

factor = 2
m = im.shape[0]
n = im.shape[1]
mp = m*factor
np = n*factor

#output = np.zeros(shape=(mp, np))
output = [[0 for _ in range(np)]for _ in range(mp)] 
print(len(output),len(output[0]))

for i in range(m):
    for j in range(n):
        output[i*factor][j*factor] = im[i][j]
        queue = deque()
        queue.append((i*factor, j*factor))
        iter = factor//2
        visited = set()
        visited.add((i*factor, j*factor))
        while queue and iter:
            temp = deque()
            while queue:
                a,b = queue.popleft()
                for x,y in ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)):
                    if 0<=a+x<m*factor and 0<=b+y<n*factor and not(a+x, b+y) in visited: 
                        temp.append((a+x, b+y))
                        visited.add((a+x, b+y))
                        output[a+x][b+y] = output[i*factor][j*factor]
            iter-=1

outputImage = Image.fromarray(numpy.array(output), "L")
outputImage.save("DecopressionRosa.jpeg")

