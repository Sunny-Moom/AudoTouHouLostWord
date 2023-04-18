import os
import subprocess
import sys
import time
from PIL import Image
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 关卡名
text = '规则'


# 定义一个函数，接受一个图片路径和一个词作为参数
def get_word_coordinates(image_path, word):
    # 读取图片文件
    img = Image.open(image_path)

    # 设置tesseract命令行参数
    config = "-l chi_sim --oem 1 --psm 3"

    # 调用image_to_data方法，返回一个字典列表
    data = pytesseract.image_to_data(img, config=config, output_type=pytesseract.Output.DICT)

    # 遍历字典列表，检查是否有匹配的词
    for i in range(len(data["text"])):
        if data["text"][i] == word:
            # 返回词的坐标，格式为(x,y,w,h)
            return data["left"][i], data["top"][i]

    # 如果没有匹配，返回None
    return None


# 使用adb截图
def adb_image():
    subprocess.call("adb shell screencap -p /sdcard/screen.png", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("adb pull /sdcard/screen.png ./img/screen.png", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("adb shell rm /sdcard/screen.png", shell=True, stdout=subprocess.DEVNULL)


# OCR识别点击
def find_and_click():
    # 加载图像

    adb_image()
    center = get_word_coordinates('./img/screen.png', text)
    if center is not None:
        print("\033[32m" + "找到匹配图像，中心点坐标为：" + "\033[0m", center)
        sys.stdout.write("\033[F")  # 光标上移一行
        sys.stdout.write("\033[K")  # 清除当前行
        # 模拟点击
        subprocess.call("adb shell input tap {} {}".format(center[0], center[1]), shell=True, stdout=subprocess.DEVNULL)
    else:
        print("\033[31m" + f"未找到匹配图像，3秒后重新查找" + "\033[0m")
        time.sleep(3)
        sys.stdout.write("\033[F")  # 光标上移一行
        sys.stdout.write("\033[K")  # 清除当前行
        find_and_click()


# 图像识别并点击
def match_image(template_file, num, cold):
    # 加载图像
    adb_image()
    img_rgb = cv2.imread('./img/screen.png')
    img_template = cv2.imread('./img/' + template_file + '/' + str(num) + '.png')
    w, h = img_template.shape[:-1]

    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(img_rgb, img_template, cv2.TM_CCOEFF_NORMED)

    # 匹配图像的坐标
    loc = np.where(result >= 0.8)

    if len(loc[0]) > 0:
        # 计算匹配图像的中心点
        center = (loc[1][0] + w // 2, loc[0][0] + h // 2)
        print("\033[32m" + "找到匹配图像，中心点坐标为：" + "\033[0m", center)
        sys.stdout.write("\033[F")  # 光标上移一行
        sys.stdout.write("\033[K")  # 清除当前行
        # 模拟点击
        subprocess.call("adb shell input tap {} {}".format(center[0], center[1]), shell=True, stdout=subprocess.DEVNULL)
    else:
        print("\033[31m" + f"未找到匹配图像，{cold} 秒后重新查找" + "\033[0m")
        sys.stdout.write("\033[F")  # 光标上移一行
        sys.stdout.write("\033[K")  # 清除当前行
        time.sleep(cold)
        match_image(template_file, num, cold)


# 加载上场角色池，关卡图
def rename_files(path):
    # 获取所有文件名
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # 对文件名进行重命名，后缀名为txt，因为直接重命名可能会导致文件名重复而报错
    for i, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, str(i) + '.txt'))

    # 获取所有文件名
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # 将文件后缀名命名回png
    for i, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, str(i) + '.png'))

    # 返回文件数量
    return len(files)


match_image("player_2", 8, 1)
