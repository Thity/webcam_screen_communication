from crop import*
from file_name_image_decoding import*
from tools import *
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance


## # # CODE FOR TESTING
#
def testCrop(file_name, borders, num=0):

    img = Image.open(file_name)
    source_img = img.convert("RGBA")
    draw = ImageDraw.Draw(source_img)

    for (top, bottom) in borders:
        draw.rectangle((top, bottom), fill="white")

    source_img.save('starts/cropTest' + str(num) + '.png', "PNG")

def partitionTest(file_name, borders, num =0):
    img = Image.open(file_name)
    source_img = img.convert("RGBA")
    draw = ImageDraw.Draw(source_img)

    bordersOfSubQuadrant = getBordersOfSubQuadrant(borders, v_part, h_part)
    itr = 0
    for (top, bottom) in bordersOfSubQuadrant[0]:

        if itr % 2 == 0:
            draw.rectangle((top, bottom), fill="white")
        else:
            draw.rectangle((top, bottom), fill="red")
        itr = itr + 1
    source_img.save('partitionTest' + str(num) + '.png', "PNG")

file_path = 'shots/pic'
extension = '.png'
start_seq = 1
end_seq = 74
images = []

for index in range(start_seq, end_seq + 1):
    filename = file_path + str(index) + extension

    images.append(file_path + str(index) + extension)
 



coding = 30
v_part = 4
h_part = 6

decodedMesage = decodeImage(images, alphabetLength, coding, v_part, h_part)
print(decodedMesage)


# # # Crop and Partition Tests

images = []

itr = 1
for testFile in images:
	img = Image.open(testFile)
	arr = np.array(img)
	dim = arr.shape
	#
	borders = getAllBorders(arr, dim)

	#
	#
	testCrop(testFile, borders, itr)
	itr+=1


