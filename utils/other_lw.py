import utils.adb_lw as adb
from PIL import Image


def crop_image(left_top_x, left_top_y, wh, output_path):
    adb.adb_image()
    # 打开图片
    img = Image.open('./data/img/screen.png')

    # 定义裁剪区域
    box = (left_top_x, left_top_y, left_top_x + wh, left_top_y + wh)

    # 裁剪图片
    cropped_img = img.crop(box)

    # 保存裁剪后的图片
    cropped_img.save('./data/img/pl/' + output_path + '.png')


def search_pl():
    for h in range(7):
        t = 43 + (h * 260)
        crop_image(t, 150, 213, str(h))
        crop_image(t, 620, 213, str(h + 7))
