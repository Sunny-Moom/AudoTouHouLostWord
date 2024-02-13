from rapidocr_onnxruntime import RapidOCR
import utils.adb_lw as adb


def find_text_in_image(target_word):
    adb.adb_image()
    engine = RapidOCR()
    img_path = './data/img/screen.png'
    result, res = engine(img_path, use_det=True, use_cls=False, use_rec=True)
    for line in result:
        if target_word in line[1]:
            text, bbox = line[1], line[0]
            center_x = (bbox[0][0] + bbox[2][0]) // 2
            center_y = (bbox[0][1] + bbox[2][1]) // 2
            adb.adb_touch(center_x, center_y)
