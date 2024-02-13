import os
import subprocess
import sys
import time
from PIL import Image
import cv2
import numpy as np

# 关卡名
play_text = '姐妹'


# def get_word_coordinates(image_path, word):
#     """
#     调用tesseract识别图片内文字并将指定文字坐标输出
#     :param image_path: 需要识别的图片
#     :param word: 需要在图片中识别的文字
#     :return: 返回词的坐标，格式为(x,y,w,h)，如果没有匹配，返回None
#     """
#     # 读取图片文件
#     img = Image.open(image_path)

#     # 设置tesseract命令行参数
#     config = "-l chi_sim --oem 1 --psm 3"

#     # 调用image_to_data方法，返回一个字典列表
#     data = pytesseract.image_to_data(img, config=config, output_type=pytesseract.Output.DICT)

#     # 遍历字典列表，检查是否有匹配的词
#     for i in range(len(data["text"])):
#         if data["text"][i] == word:
#             # 返回词的坐标，格式为(x,y,w,h)
#             return data["left"][i], data["top"][i]

#     # 如果没有匹配，返回None
#     return None


def adb_image():
    """
    使用adb截图
    :return: 将截图输出至.img/screen.png
    """
    subprocess.call("adb shell screencap -p /sdcard/screen.png", shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("adb pull /sdcard/screen.png ./img/screen.png", shell=True, stdout=subprocess.DEVNULL)


def image(template_file, num, tep=0.8):
    # 加载图像
    adb_image()
    img_rgb = cv2.imread('./img/screen.png')
    img_template = cv2.imread('./img/' + template_file + '/' + str(num) + '.png')
    w, h = img_template.shape[:-1]

    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(img_rgb, img_template, cv2.TM_CCOEFF_NORMED)

    # 匹配图像的坐标
    loc = np.where(result >= tep)
    re = [w, h, loc]
    return re


# def find_and_click(text):
#     """
#     实现点击指定文字
#     :param text: 需要点击的文字
#     :return: 无输出
#     """
#     while True:
#         adb_image()
#         center = get_word_coordinates('./img/screen.png', text)
#         if center is not None:
#             print("\033[32m" + "找到匹配图像，中心点坐标为：" + "\033[0m", center)
#             sys.stdout.write("\033[F")  # 光标上移一行
#             sys.stdout.write("\033[K")  # 清除当前行
#             # 模拟点击
#             subprocess.call("adb shell input tap {} {}".format(center[0], center[1]), shell=True,
#                             stdout=subprocess.DEVNULL)
#             break
#         else:
#             print("\033[31m" + f"未找到匹配图像，3秒后重新查找" + "\033[0m")
#             time.sleep(3)
#             sys.stdout.write("\033[F")  # 光标上移一行
#             sys.stdout.write("\033[K")  # 清除当前行


def match_image(template_file, num, cold, tep=0.8):
    """
    使用opencv实现图像识别并点击
    :param template_file: ./img文件夹内图像所处的文件夹名
    :param num: 需要点击的图像的编号
    :param cold: 未找到图像后暂停时间
    :return: 无输出
    """
    while True:
        re = image(template_file, num, tep)
        w = re[0]
        h = re[1]
        loc = re[2]
        if len(loc[0]) > 0:
            # 计算匹配图像的中心点
            center = (loc[1][0] + w // 2, loc[0][0] + h // 2)
            print("\033[32m" + "找到匹配图像，中心点坐标为：" + "\033[0m", center)
            sys.stdout.write("\033[F")  # 光标上移一行
            sys.stdout.write("\033[K")  # 清除当前行
            # 模拟点击
            subprocess.call("adb shell input tap {} {}".format(center[0], center[1]), shell=True,
                            stdout=subprocess.DEVNULL)
            break
        else:
            print("\033[31m" + f"未找到匹配图像，{cold} 秒后重新查找" + "\033[0m")
            sys.stdout.write("\033[F")  # 光标上移一行
            sys.stdout.write("\033[K")  # 清除当前行
            time.sleep(cold)


def search_image(template_file, num, tim, tep=0.8):
    """
    查找屏幕内是否出现指定图像
    :param tep:
    :param template_file: ./img文件夹内图像所处的文件夹名
    :param num: 需要查找的图像的编号
    :param tim: 查找的次数（1秒1次）
    :return: 如果找到，输出坐标，如果没找到,输出False
    """
    t = True
    while t:
        re = image(template_file, num, tep)
        w = re[0]
        h = re[1]
        loc = re[2]

        if len(loc[0]) > 0:
            # 计算匹配图像的中心点
            center = (loc[1][0] + w // 2, loc[0][0] + h // 2)
            print("\033[32m" + "找到匹配图像，中心点坐标为：" + "\033[0m", center)
            sys.stdout.write("\033[F")  # 光标上移一行
            sys.stdout.write("\033[K")  # 清除当前行
            t = False
            return center
        else:
            if tim == 0:
                print("\033[31m" + "未找到匹配图像，直接进行下一步" + "\033[0m")
                sys.stdout.write("\033[F")  # 光标上移一行
                sys.stdout.write("\033[K")  # 清除当前行
                t = False
                return False
            tim -= 1
            time.sleep(1)


def press(center, tim):
    """
    模拟长按
    :param center: 长按坐标
    :param tim: 长按时间
    :return: 无输出
    """
    tim = tim * 1000
    subprocess.call(
        "adb shell input touchscreen swipe {} {} {} {} {}".format(center[0], center[1], center[0], center[1], tim),
        shell=True, stdout=subprocess.DEVNULL)
    print("\033[32m" + "已执行长按坐标：" + "\033[0m", center)
    sys.stdout.write("\033[F")  # 光标上移一行
    sys.stdout.write("\033[K")  # 清除当前行


def tap(center):
    """
    模拟点击
    :param center: 点击坐标
    :return:
    """
    print("\033[32m" + "已执行点击坐标：" + "\033[0m", center)
    sys.stdout.write("\033[F")  # 光标上移一行
    sys.stdout.write("\033[K")  # 清除当前行
    # 模拟点击
    subprocess.call("adb shell input tap {} {}".format(center[0], center[1]), shell=True, stdout=subprocess.DEVNULL)


def row(center, x, y, tim):
    cd = [0, 0]
    cd[0] = center[0] + x
    cd[1] = center[1] + y
    subprocess.call(
        "adb shell input touchscreen swipe {} {} {} {} {}".format(center[0], center[1], cd[0], cd[1], tim*1000),
        shell=True, stdout=subprocess.DEVNULL)


def search_tap(template_file, num, tim, cold):
    """
    搜索图片，如果有就点击，无就略过
    :param template_file:
    :param num:
    :param tim:
    :param cold:
    :return:
    """
    center = search_image(template_file, num, tim)
    if center:
        tap(center)
        time.sleep(cold)


def rename_files(path):
    """
    将图像进行随机编号并输出图像数量
    :param path: 需要编号的目录
    :return: 图像的数量
    """
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


def image_all(template_file, num):
    # 加载图像
    adb_image()
    img_rgb = cv2.imread('./img/screen.png')
    img_template = cv2.imread('./img/' + template_file + '/' + str(num) + '.png')
    w, h = img_template.shape[:-1]

    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(img_rgb, img_template, cv2.TM_CCOEFF_NORMED)

    # 匹配图像的坐标
    loc = np.where(result >= 0.8)
    return loc, w, h


def search_image_all(template_file, num, tim):
    """
    查找屏幕内是否出现指定图像
    :param template_file: ./img文件夹内图像所处的文件夹名
    :param num: 需要查找的图像的编号
    :param tim: 查找的次数（1秒1次）
    :return: 如果找到，输出所有匹配图像的中心点坐标，如果没找到,输出False
    """
    t = True
    while t:
        loc, w, h = image_all(template_file, num)

        if len(loc[0]) > 0:
            # 计算匹配图像的中心点
            centers = []
            for pt in zip(*loc[::-1]):
                center = (pt[0] + w // 2, pt[1] + h // 2)
                centers.append(center)
            t = False
            return centers
        else:
            if tim == 0:
                t = False
                return False
            tim -= 1
            time.sleep(1)
