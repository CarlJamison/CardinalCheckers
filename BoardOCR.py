from PIL import Image

def checkHist(hist, threshold = 90):
    total = 0
    for val in hist[128:]:
        total += val
    return total > threshold

def getValueAt(image, i, j):
    cropped = image.crop((i * 16, j * 16, (i + 1) * 16, (j + 1) * 16))
    red = checkHist(cropped.split()[0].histogram())
    blue = checkHist(cropped.split()[1].histogram())
    green = checkHist(cropped.split()[2].histogram())

    retVal = 0
    
    if(red):
        retVal += 1
    
    if(blue):
        retVal += 2

    if(green): 
        retVal += 4

    if(retVal == 3):
        if(checkHist(cropped.split()[0].histogram(), 128)):
            retVal += 1

    return retVal

img = Image.open('boardtest.jpg') 

#img = img.transform((512, 512), Image.AFFINE, (1, 1, 0, 0, 1, 0))
#img = img.transform((128, 128), Image.QUAD, (180, 80, 3350, 90, 3380, 3350, 90, 3350))
img = img.transform((128, 128), Image.QUAD, (90, 3350, 3380, 3350, 3350, 90, 180, 80))   

printString = "2"
for i in range(8):
    printString += " "
    for j in range(8):
        if((i + j) % 2 == 0):
            val = getValueAt(img, j, i)
            if(val == 0):
                printString += "2-"
            elif(val == 1):
                printString += "0-"
            elif(val == 3):
                printString += "2C"
            elif(val == 4):
                printString += "0C"
            elif(val == 7):
                printString += "1-"

print(printString)