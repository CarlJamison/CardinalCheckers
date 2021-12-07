from PIL import Image

def checkHist(hist, threshold = 90):
    total = 0
    for val in hist[100:]:
        total += val
    return total > threshold

def getValueAt(image, i, j):
    cropped = image.crop((i * 16, j * 16, (i + 1) * 16, (j + 1) * 16))
    red = checkHist(cropped.split()[0].histogram(), 120)
    blue = checkHist(cropped.split()[1].histogram(), 120)
    #green = checkHist(cropped.split()[2].histogram())

    retVal = 0
    
    if(red):
        retVal += 1
    
    if(blue):
        retVal += 2

    if(blue): 
        retVal += 4

    if(retVal == 3):
        if(checkHist(cropped.split()[0].histogram(), 128)):
            retVal += 1
    return retVal

def getBoardString(img):
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
                else:
                    printString += "1-"
    return printString

def locateCorner(img):
    hist = img.split()
    iTotal = 0
    jTotal = 0
    counter = 0
    for i in range(img.width):
        for j in range(img.height):
            if hist[2].getpixel((i, j)) > 100 and hist[2].getpixel((i, j)) > 1.5 * hist[0].getpixel((i, j)):
                iTotal += i
                jTotal += j
                counter += 1
    return (iTotal / counter, jTotal / counter)

def getBoardStringFromImage(fileName):
    img = Image.open(fileName)
    #img = img.resize((int(img.width / 4), int(img.height / 4)))
    cropped = img#.crop((1800, 0, img.width, img.height))
    ulCorner = locateCorner(cropped.crop((0, 0, cropped.width / 2, cropped.height / 2)))
    urCorner = locateCorner(cropped.crop((cropped.width / 2, 0, cropped.width, cropped.height / 2)))
    llCorner = locateCorner(cropped.crop((0, cropped.height / 2, cropped.width / 2, cropped.height)))
    lrCorner = locateCorner(cropped.crop((cropped.width / 2, cropped.height / 2, cropped.width, cropped.height)))

    o = 8 

    cropped = cropped.transform((128, 128), Image.QUAD, 
        (llCorner[0] + o, llCorner[1] - o + cropped.height / 2,
        lrCorner[0] - o + cropped.width / 2,  lrCorner[1] - o + cropped.height / 2,
        urCorner[0] - o + cropped.width / 2, urCorner[1] + o, 
        ulCorner[0] + o, ulCorner[1] + o))  
    cropped = cropped.rotate(90)
    cropped.save('test.jpg')

    boardString = getBoardString(cropped)
    print(boardString)
    return boardString