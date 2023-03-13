from typing import List, Tuple
from PIL import Image, ImageDraw
import paddleocr
import os

image_path: str = "test-files/ticket-de-caisse-5.png"

# compute path of output image and text
extension: str = os.path.splitext(image_path)[1]
assert extension == ".png", ".png format is required"
image_path_without_extension: str = os.path.splitext(image_path)[0]
ocrised_image_path: str = image_path_without_extension + "_OCRised.png"
ocrised_text_path: str = image_path_without_extension + "_OCRised_text.txt"


# load OCR model
ocrModel = paddleocr.PaddleOCR(use_angle_cls=False, lang='fr')

# run OCR model
ocrResult: List[List[List | Tuple]] = ocrModel.ocr(image_path, cls=False)

# Draw boxes and save text
with Image.open(image_path) as image:
    draw = ImageDraw.Draw(image)
    textFile = open(ocrised_text_path, "w")

    for boxCoordinates, textAndScore in ocrResult[0]:
        xLeft, xRight, yLow, yHigh = boxCoordinates[0][0], boxCoordinates[1][0], boxCoordinates[0][1], boxCoordinates[2][1]
        draw.line(xy=(xLeft, yLow, xRight, yLow), fill="red")
        draw.line(xy=(xRight, yLow, xRight, yHigh), fill="red")
        draw.line(xy=(xRight, yHigh, xLeft, yHigh), fill="red")
        draw.line(xy=(xLeft, yHigh, xLeft, yLow), fill="red")
        textFile.write(textAndScore[0] + "\n")

    image.save(ocrised_image_path, "PNG")
    textFile.close()
