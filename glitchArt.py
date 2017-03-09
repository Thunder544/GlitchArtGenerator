from PIL import Image
import random

#NOTE: Color index can only be 0,1 or 2
def sortBy(colorTuple, colorIndex, reverse):
    if reverse:
        return sorted(colorTuple, key=lambda x: x[colorIndex], reverse=reverse)
    else:
        return sorted(colorTuple, key=lambda x: x[colorIndex])


#NOTE: Image file must be in same directory as this script
fileName = "YOUR FILENAME HERE"
outputFileName = "WHATEVER YOU WANT TO CALL IT"

img = Image.open(fileName)

imgList = list(img.getdata())
loadImg = img.load()
loadImgList = []
loadImgList2 = []

width, height = img.size

startWidth = random.randint(0, (width-150))
startHeight = random.randint(0, (height-75))

for i in range(startWidth, startWidth+150):
    for j in range(height):
        loadImgList.append(loadImg[i, j])


for i in range(width):
    for j in range(startHeight, startHeight+75):
        loadImgList2.append(loadImg[i, j])

loadImgList = sortBy(loadImgList, 2, False)
loadImgList = sortBy(loadImgList, 1, False)
loadImgList = sortBy(loadImgList, 0, False)


loadImgList2 = sortBy(loadImgList2, 2, True)
loadImgList2 = sortBy(loadImgList2, 1, True)
loadImgList2 = sortBy(loadImgList2, 0, True)


counter = 0

for i in range(startWidth, startWidth+150):
    for j in range(height):
        loadImg[i, j] = loadImgList[counter]
        counter += 1


counter = 0

for i in range(width):
    for j in range(startHeight, startHeight+75):
        loadImg[i, j] = loadImgList2[counter]
        counter += 1

img.show()

img.save(outputFileName)
