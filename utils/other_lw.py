import os
import sys
import time

import utils.adb_lw as adb
import utils.cv_lw as cv
from PIL import Image


def progress_bar(duration):
    """显示一个在指定时间内填充的进度条。

    Args:
        duration (int): 进度条完成所需的总秒数。
    """
    sys.stdout.write("[")
    sys.stdout.flush()
    for i in range(duration):
        sys.stdout.write("=")  # 或使用其他字符来表示进度
        sys.stdout.flush()
        time.sleep(1)  # 等待一秒
    sys.stdout.write("]\n")  # 进度条结束


def crop_image(left_top_x, left_top_y, w, h, output_path):
    adb.adb_image()
    # 打开图片
    img = Image.open('./data/img/screen.png')

    # 定义裁剪区域
    box = (left_top_x, left_top_y, left_top_x + w, left_top_y + h)

    # 裁剪图片
    cropped_img = img.crop(box)

    # 保存裁剪后的图片
    cropped_img.save('./data/img/' + output_path + '.png')


def search_pl():
    for h in range(7):
        t = 43 + (h * 260)
        crop_image(t, 150, 213, 213, "pl/"+str(h))
        crop_image(t, 620, 213, 213, "pl/"+str(h + 7))


# print(cv.load_and_match_image("fs", 1))