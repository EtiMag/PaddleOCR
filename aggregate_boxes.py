import paddleocr

image_path: str = "test-files/ppocr_img/table/table.jpg"

ocrModel = paddleocr.PaddleOCR(use_angle_cls=False, lang='fr')

ocrResult: list[list[list[list[float]] | tuple[str, float]]] = ocrModel.ocr(image_path, cls=False)
# [img_index][textbox_index][]
print(ocrResult[0][0])
print(f"len(ocrResult[0]) = {len(ocrResult[0])}")
print(f"type(ocrResult[0][0][0]) = {type(ocrResult[0][0][0])}")
